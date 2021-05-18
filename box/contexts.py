from django.shortcuts import get_object_or_404
from products.models import Product


def box_contents(request):

    box_items = []
    product_count = 0
    box = request.session.get('box', {})

    for item_id, quantity in box.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count += quantity
        box_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'box_items': box_items,
        'product_count': product_count,
    }

    return context
