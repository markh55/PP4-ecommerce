from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
import ast

# Create your views here.
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Check if clear button was clicked
        if request.POST.get('clear_info'):
            profile.default_first_name = ''
            profile.default_surname = ''
            profile.default_phone_number = ''
            profile.default_email = ''
            profile.default_business_name = ''
            profile.save()
            messages.success(request, 'Your saved information has been cleared.')
            return redirect('profiles:profile')
        
        # Handle profile information form
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }
    return render(request, template, context)

def order_history(request, order_number):
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(profile.orders, order_number=order_number)

    # import order items from original bag
    try:
        order_items = ast.literal_eval(order.original_bag)
    except:
        order_items = []

    template = 'orders/order_details.html'
    context = {
        'order': order,
        'order_items': order_items,
        'from_profile': True,
    }

    return render(request, template, context)