from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, BoxItems
from products.models import Product

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        box = request.session.get('box', '')

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'contact_number': request.POST['contact_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id in list(box.keys()):
                product = Product.objects.get(pk=item_id)
                box_items = BoxItems(
                    order=order,
                    product=product,
                )
                box_items.save()

            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your details and try again.')
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
    # save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
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
