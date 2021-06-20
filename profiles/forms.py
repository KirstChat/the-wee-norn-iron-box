from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Add placeholders and set autofocus on first field
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_contact_number': 'Contact Number',
            'default_address_line_1': 'Address Line 1',
            'default_address_line_2': 'Address Line 2',
            'default_town_or_city': 'Town/City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_contact_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                # Add * to placeholder if field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                # Set placeholder attributes to values from dictionary above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Remove auto-generated labels
            self.fields[field].label = False
