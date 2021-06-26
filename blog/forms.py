from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'post', 'status', )
        exclude = ('posted_by', 'date_posted', )

    # def __init__(self, *args, **kwargs):
    #     # Add placeholders
    #     placeholders = {
    #         'title': 'Post Title',
    #         'post': 'Blog Post',
    #     }

    #     for field in self.fields:
    #         # Add * to placeholder if required
    #         if self.fields[field].required:
    #             placeholder = f'{placeholders[field]}*'
    #         else:
    #             placeholder = placeholders[field]
    #         # Set placeholder attribute to values from dictionary above
    #         self.fields[field].widget.attrs['placeholder'] = placeholder
    #         self.fields[field].label = False
