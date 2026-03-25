from django import forms
from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle']
        labels = {'title': 'Title', 'subtitle': 'Subtitle'}


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']
        labels = {'title': 'Post Title', 'body': ''}
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}
