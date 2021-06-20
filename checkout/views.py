from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, BoxItems
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        # Payment Intent ID
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'box': json.dumps(request.session.get('box', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment can\'t be processed right now.\
            Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        box = request.session.get('box', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'contact_number': request.POST['contact_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_box = json.dumps(box)
            order.save()
            for item_id in list(box.keys()):
                product = Product.objects.get(pk=item_id)
                box_items = BoxItems(
                    order=order,
                    product=product,
                )
                box_items.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your details and try again.')
            return redirect('checkout')
    else:
        box = request.session.get('box', {})
        if not box:
            messages.error(
                request, 'You haven\'t added anything to your wee box!')
            return redirect(reverse('products'))

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=settings.FIXED_PRICE,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'contact_number': profile.default_contact_number,
                    'address_line_1': profile.default_address_line_1,
                    'address_line_2': profile.default_address_line_2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing! \
            Did you forget to set it in you environment?')

    if len(list(box.keys())) < 6:
        return redirect(reverse('view_box'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    # Handle Successful Checkout
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_contact_number': order.contact_number,
                'default_address_line_1': order.address_line_1,
                'default_address_line_2': order.address_line_2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your order was successful!\
        Your order number is {order_number}. A confirmation email\
            has been sent to {order.email}')

    if 'box' in request.session:
        del request.session['box']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
