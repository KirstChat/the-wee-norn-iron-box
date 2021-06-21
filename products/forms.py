from django import forms
from .widgets import CustomClearableFileInput
from .models import Category, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List Comprehension
        names = [(c.id, c.get_name()) for c in categories]

        self.fields['category'].choices = names
