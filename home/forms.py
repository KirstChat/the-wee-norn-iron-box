from django import forms
from django.utils.safestring import mark_safe
from .models import Review

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import InlineRadios


class ReviewForm(forms.ModelForm):
    # Code from django docs & stack overflow:
    # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
    # https://stackoverflow.com/questions/52436319/how-to-display-markup-instead-of-pure-text-in-django-form
    rating = forms.TypedChoiceField(
        choices=(
            (1, mark_safe('<i class="fas fa-star"></i>\
                    - Extremely Disappointed')),
            (2, mark_safe('<i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i> - Disappointed')),
            (3, mark_safe('<i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i> - Neutral')),
            (4, mark_safe('<i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i> - Happy')),
            (5, mark_safe('<i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i>\
                    <i class="fas fa-star"></i> - Extremely Happy!'))
            ),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Review
        fields = ['review', 'rating']
        exclude = ['posted_by']
        widgets = {
            'review': forms.Textarea(attrs={
                'placeholder': 'Leave your review here...'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Code from crispy forms docs:
        # https://django-crispy-forms.readthedocs.io/en/latest/index.html
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                InlineRadios('rating'),
            ),
        )
