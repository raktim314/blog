from base.models import Blog, Comment
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')