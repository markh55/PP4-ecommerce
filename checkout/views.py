from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from packages.models import Package

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('packages:package_list'))

    services_summary = []
    total = 0
    for package_id in bag.keys():
        package = Package.objects.get(pk=package_id)
        services_summary.append({
            'id': package.id,
            'name': package.name,
            'image': package.image,
            'price': float(package.price),
            'quantity': bag.get(package_id, 1)
        })
        total += float(package.price) * services_summary[-1]['quantity']

    if request.method == 'POST':
        order_summary = []
        for item in services_summary:
            order_summary.append({
                'id': item['id'],
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity'],
                'image_url': item['image'].url if item['image'] else None
            })

        request.session['order_summary'] = {
            'services_summary': order_summary,
            'grand_total': total
        }
        request.session['bag'] = {}
        return redirect('checkout:checkout_success')

    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),
        currency='gbp',
    )

    context = {
        'services_summary': services_summary,
        'total': total,
        'grand_total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


@login_required
def checkout_success(request):
    order_summary = request.session.pop('order_summary', None)
    context = {
        'services_summary': order_summary['services_summary'] if order_summary else [],
        'grand_total': order_summary['grand_total'] if order_summary else 0,
    }
    return render(request, 'checkout/checkout_success.html', context)
