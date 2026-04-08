from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    """A model representing the overall blog."""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

class BlogPost(models.Model):
    """An individual blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blog_posts'

    def __str__(self):
        """Return a string representation of the post title."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title