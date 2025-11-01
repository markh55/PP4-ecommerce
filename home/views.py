from django.shortcuts import render
from django.core.mail import send_mail
from packages.models import Package, Review
from .forms import ContactForm, SubscriberForm

# Home page
def index(request):
    packages = Package.objects.all()[:4]

    # Show recent reviews on the homepage
    recent_reviews = Review.objects.select_related('package', 'user').order_by('-created_at')[:5]

    form_success = None  # Track form submission success

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
            # Indicate success to display message in form
            form_success = "Thank you for your message. A member of the team will get back to you."
            form = ContactForm()  # Reset form after submission
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {
        'packages': packages,
        'form': form,
        'recent_reviews': recent_reviews,
        'form_success': form_success,
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
        # You can leave subscription messages as is or remove them
    return render(request, 'home/index.html', {'form': SubscriberForm()})

# Static pages
def faq(request):
    return render(request, 'home/faq.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')

def error_404_view(request, exception):
    return render(request, 'core/404.html', status=404)
