from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import BoxItems, Order
from products.models import Product
from profiles.models import UserProfile

import json
import time


class Stripe_Handler:
    # Handle Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        # Send the user confirmation email
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        # Handle a generic/unknown/unexpected webhook event
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        # Handle Stripe payment_intent.succeeded webhook
        intent = event.data.object
        pid = intent.id
        box = intent.metadata.box
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping

        # Clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        # Update profile information if save_info is checked
        profile = None
        username = intent.metadata.username
        if username:
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_contact_number = shipping_details.phone
                profile.default_address_line_1 = shipping_details.address.line1
                profile.default_address_line_2 = shipping_details.address.line2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    contact_number__iexact=shipping_details.phone,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    original_box=box,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                        | SUCCESS: verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.name,
                    contact_number=shipping_details.address.phone,
                    address_line_1=shipping_details.address.line1,
                    address_line_2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_box=box,
                    stripe_pid=pid,
                )
                for item_id in json.loads(box).items():
                    product = Product.objects.get(pk=item_id)
                    box_items = BoxItems(
                        order=order,
                        product=product,
                    )
                    box_items.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} \
                        | ERROR: {e}, status=500')
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Created order in webhook')

    def handle_payment_intent_payment_failed(self, event):
        # Handle Stripe payment_intent.payment_failed webhook
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
