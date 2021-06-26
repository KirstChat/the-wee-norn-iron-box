from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'post']
        exclude = ['posted_by', 'date_posted']

    def __init__(self, *args, **kwargs):
        # Add placeholders
        placeholders = {
            'title': 'Post Title',
            'post': 'Blog Post',
        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
