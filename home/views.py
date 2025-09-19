from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from packages.models import Package
from .forms import ContactForm

# Home page
def index(request):
    packages = Package.objects.all()[:4]

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
            messages.success(request, "Thank you for your message. A member of the team will get back to you.")
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {
        'packages': packages,
        'form': form,
    })

# Packages page
def packages(request):
    packages = Package.objects.all()
    return render(request, 'home/packages.html', {'packages': packages})
