from django.shortcuts import render, redirect
from django.contrib import messages
from packages.models import Package

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, items_id):
    package = Package.objects.get(id=items_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if items_id in list(bag.keys()):
        bag[items_id] += quantity
        messages.success(request, f'Updated {package.name} quantity in your bag')
    else:
        bag[items_id] = quantity
        messages.success(request, f'Added {package.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, items_id):
    """ Remove an item from the shopping bag """
    bag = request.session.get('bag', {})

    items_id = str(items_id)
    if items_id in bag:
        del bag[items_id]
        request.session['bag'] = bag
        messages.success(request, 'Item removed from your bag')

    return redirect('bag:view_bag')
