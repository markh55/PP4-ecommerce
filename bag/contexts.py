from django.conf import settings

def bag_contents(request):
    context = {}

    bag_items = []
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context

