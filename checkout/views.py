from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from packages.models import Package

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

    context = {
        'services_summary': services_summary,
        'total': total,
        'grand_total': total,
        'stripe_public_key': 'pk_test_51RxZrIJDNpQfwITIBNzdHHtSpMiKd1j704EBaWx8dTlLQLY9DfaVWUJYLEZFegHT1s5ovLo7wcUXAv0TlrjDmIZL00Ekdcxt6M',
    }

    return render(request, 'checkout/checkout.html', context)