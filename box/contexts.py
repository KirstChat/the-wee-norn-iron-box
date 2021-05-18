def box_contents(request):

    box_items = []
    product_count = 0

    context = {
        'box_items': box_items,
        'product_count': product_count,
    }

    return context
