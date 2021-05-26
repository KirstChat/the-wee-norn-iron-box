from django.shortcuts import get_object_or_404
from products.models import Product


def box_contents(request):

    box_items = []
    box = request.session.get('box', {})

    for item_id, category in box.items():
        product = get_object_or_404(Product, pk=item_id)
        category = product.category
        box_items.append({
            'product': product,
            'item_id': item_id,
            'category': category,
        })

    context = {
        'box_items': box_items,
        }

    return context
