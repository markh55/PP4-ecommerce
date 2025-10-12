from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_business_name': 'Business Name (Optional)',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            field.label = False
            placeholder = placeholders.get(field_name, '')
            if field.required:
                placeholder += ' *'
            field.widget.attrs['placeholder'] = placeholder