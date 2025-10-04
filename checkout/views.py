from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from packages.models import Package
from .forms import CheckoutForm
from .models import Order, OrderLineItem


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:products'))

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                first_name=form.cleaned_data['first_name'],
                surname=form.cleaned_data['surname'],
                business_name=form.cleaned_data['business_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                preferred_contact_method=form.cleaned_data['preferred_contact_method'],
                preferred_contact_time=form.cleaned_data['preferred_contact_time'],
                additional_notes=form.cleaned_data['additional_notes'],
            )
            for package_id, quantity in bag.items():
                package = Package.objects.get(pk=package_id)
                OrderLineItem.objects.create(
                    order=order,
                    package=package,
                    quantity=1
                )
            request.session['bag'] = {}
            return redirect(reverse('checkout:checkout_success'))
        else:
            messages.error(request, "There was an error with your form. Please check your details.")

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
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'form': CheckoutForm(),
    }

    return render(request, 'checkout/checkout.html', context)


@login_required
def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')
