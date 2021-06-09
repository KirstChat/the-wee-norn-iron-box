from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

import stripe

# Create your views here.


def checkout(request):
    box = request.session.get('box', {})

    if not box:
        messages.error(request, 'You haven\'t added anything to your wee box!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ITBQLAMYLVibdjZUpRFyT5zA5ZEaidGAc7LkAhnNe8jGoZaYsjg2BeVfstKvGPBuiGmprXizchISIZlqYRqMbtp00pg9y5UdT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
