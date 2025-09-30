from django import forms

CONTACT_METHOD_CHOICES = [
    ('email', 'Email'),
    ('phone', 'Phone'),
]

CONTACT_TIME_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
]

class CheckoutForm(forms.Form):
    # Details
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    surname = forms.CharField(max_length=50, required=True, label='Surname')
    business_name = forms.CharField(max_length=100, required=False, label='Business Name (Optional)')

    # Contact Information
    email = forms.EmailField(required=True, label='Email Address')
    phone_number = forms.CharField(max_length=20, required=True, label='Phone Number')
    preferred_contact_method = forms.ChoiceField(choices=CONTACT_METHOD_CHOICES, required=False, label='Preferred Contact Method')
    preferred_contact_time = forms.ChoiceField(choices=CONTACT_TIME_CHOICES, required=False, label='Preferred Contact Time')
    additional_notes = forms.CharField(widget=forms.Textarea, required=False, label='Additional Notes (Optional)')
