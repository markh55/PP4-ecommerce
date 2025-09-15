from django.shortcuts import render, redirect
from django.core.mail import send_mail
from packages.models import Package
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Name *",
            "required": True,
            "class": "form-control",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email Address *",
            "required": True,
            "class": "form-control",
        })
    )
    number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Phone Number",
            "class": "form-control",
        })
    )
    inquiry_type = forms.ChoiceField(
        choices=[
            ("", "Select Inquiry Type *"),
            ("Packages", "Packages"),
            ("Call Back", "Request a callback"),
            ("other", "Other"),
        ],
        widget=forms.Select(attrs={
            "required": True,
            "class": "form-control",
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 6,
            "placeholder": "Type your message...",
            "required": True,
            "class": "form-control",
        })
    )

def index(request):
    packages = Package.objects.all()[:4]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"New Inquiry: {form.cleaned_data['inquiry_type']}",
                message=(
                    f"Name: {form.cleaned_data['name']}\n"
                    f"Email: {form.cleaned_data['email']}\n"
                    f"Phone: {form.cleaned_data.get('number', 'N/A')}\n\n"
                    f"Message:\n{form.cleaned_data['message']}"
                ),
                from_email=form.cleaned_data["email"],
                recipient_list=["enquire.webworks@gmail.com"],
            )
            return redirect("index")
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {
        'packages': packages,
        'form': form,
    })

def packages(request):
    packages = Package.objects.all()
    return render(request, 'home/packages.html', {'packages': packages})
