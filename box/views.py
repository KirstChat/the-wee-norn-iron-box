from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product

# Create your views here.


@login_required
def view_box(request):
    # A view that renders the box contents

    return render(request, 'box/box.html')


@login_required
def add_to_box(request, item_id):
    # Add product to box

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1  # Default value
    redirect_url = request.POST.get('redirect_url')

    box = request.session.get('box', {})

    if item_id in box:
        messages.error(
            request, f'You\'ve already added {product.name} to your box')
    else:
        box[item_id] = quantity
        messages.success(request, f'You\'ve added {product.name} to your box!')

    request.session['box'] = box
    print(request.session['box'])
    return redirect(redirect_url)


@login_required
def remove_from_box(request, item_id):
    # Remove product from box

    try:
        product = get_object_or_404(Product, pk=item_id)
        box = request.session.get('box', {})

        if item_id in box:
            box.pop(item_id)
            messages.success(
                request, f'You\'ve removed {product.name} from your box')

        request.session['box'] = box
        return redirect(reverse('view_box'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
