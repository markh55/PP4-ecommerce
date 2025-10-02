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
        return redirect(reverse('products'))

    services_summary = []
    total = 0
    for package_id in bag.keys():
        package = Package.objects.get(pk=package_id)
        services_summary.append({
            'id': package.id,
            'name': package.name,
            'image': package.image,
            'price': package.price
        })
        total += float(package.price)

    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),
        currency=settings.STRIPE_CURRENCY,
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
    return render(request, 'checkout/checkout_success.html')
