from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'contact_number',
                  'address_line_1', 'address_line_2', 'town_or_city',
                  'county', 'postcode', 'country', )

    def __init__(self, *args, **kwargs):
        # Add placeholders and set autofocus on first name field
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'contact_number': 'Contact Number',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'town_or_city': 'Town/City',
            'county': 'County',
            'postcode': 'Postcode',
        }

        set.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Add * to placeholder if field is required
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            # Set placeholder attributes to values from dictionary
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Remove auto-generated labels
            self.fields[field].label = False
