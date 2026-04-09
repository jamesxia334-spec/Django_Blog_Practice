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
        fields = ['blog', 'title', 'body']
        labels = {'blog': 'Blog', 'title': 'Post Title', 'body': ''}
        widgets = {
            'title': forms.TextInput(attrs={'size': 50}),
            'body': forms.Textarea(attrs={'cols': 80}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BlogPostForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['blog'].queryset = Blog.objects.filter(owner=self.user)
