from django import forms
from .models import Subscriber

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

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email',
                'class': 'form-control',
                'required': True,
            })
        }