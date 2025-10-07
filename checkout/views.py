from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
import json
from packages.models import Package
from checkout.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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

    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),
        currency='gbp',
    )

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

        order = Order.objects.create(
            user=request.user,
            full_name=request.POST.get('first_name') + ' ' + request.POST.get('surname'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            order_total=total,
            original_bag=str(order_summary),
            stripe_pid=intent.id
)

        request.session['bag'] = {}
        request.session['order_number'] = order.order_number
        return redirect('checkout:checkout_success')

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
    order_number = request.session.pop('order_number', None)
    order = Order.objects.filter(order_number=order_number).first()

    context = {
        'order': order,
        'services_summary': [],
        'grand_total': order.order_total if order else 0,
    }
    return render(request, 'checkout/checkout_success.html', context)
