from django import forms
from .models import Review

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import InlineRadios


class ReviewForm(forms.ModelForm):
    # Code from django docs:
    # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
    rating = forms.TypedChoiceField(
        choices=(
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars')
            ),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Review
        fields = ('title', 'review', 'rating')
        exclude = ['posted_by']

    def __init__(self, *args, **kwargs):
        # Add placeholders
        super().__init__(*args, **kwargs)
        # Code from crispy forms docs:
        # https://django-crispy-forms.readthedocs.io/en/latest/index.html
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                InlineRadios('rating'),
            ),
        )

        placeholders = {
            'title': 'Review Title',
            'review': 'Review',
            'rating': 'Rating',
        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
