from django.shortcuts import get_object_or_404
from products.models import Product


def box_contents(request):

    box_items = []
    quantity = 1
    box = request.session.get('box', {})

    for item_id, quantity in box.items():
        product = get_object_or_404(Product, pk=item_id)
        box_items.append({
            'product': product,
            'item_id': item_id,
            'quantity': quantity,
        })

    context = {
        'box_items': box_items,
        }

    return context
