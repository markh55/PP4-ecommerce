from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from packages.models import Package, Review
from .forms import ContactForm, SubscriberForm

# Home page
def index(request):
    packages = Package.objects.all()[:4]

    # Show recent reviews on the homepage
    recent_reviews = Review.objects.select_related('package', 'user').order_by('-created_at')[:5]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"New Inquiry: {form.cleaned_data['inquiry_type']}",
                message=(
                    f"Name: {form.cleaned_data['name']}\n"
                    f"Email: {form.cleaned_data['email']}\n\n"
                    f"Message:\n{form.cleaned_data['message']}"
                ),
                from_email=form.cleaned_data["email"],
                recipient_list=["youremail@example.com"],
            )
            # Add success message for visual confirmation
            messages.success(request, "Thank you for your message. A member of the team will get back to you.")
            # Redirect to prevent message showing on page refresh
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {
        'packages': packages,
        'form': form,
        'recent_reviews': recent_reviews,
    })

# Packages page
def packages(request):
    packages = Package.objects.all()
    return render(request, 'home/packages.html', {'packages': packages})


# Subscribe to newsletter
def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing to our newsletter!")
            return redirect('index')
    else:
        messages.error(request, "There was an error with your subscription. Please try again.")
        return redirect('index')
    return redirect('index')