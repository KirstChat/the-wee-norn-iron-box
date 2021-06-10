from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    box = request.session.get('box', {})
    if not box:
        messages.error(request, 'You haven\'t added anything to your wee box!')
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

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
