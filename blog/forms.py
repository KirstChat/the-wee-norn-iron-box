from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'post', 'status', )
        exclude = ('posted_by', 'date_posted', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', )
        exclude = ('posted_by', 'date_commented', )
