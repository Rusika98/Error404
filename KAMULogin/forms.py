from django import forms
from .models import Comment, BlogPosts


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","email","body"]


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = ["title","slug","intro","body"]



