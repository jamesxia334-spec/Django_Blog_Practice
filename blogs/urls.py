"""Defines URL patterns for blogs (APP)."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blogs.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single blog.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),

    # Page for adding a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new blog post.
    path('new_blog_post/<int:blog_id>/', views.new_blog_post, name='new_blog_post'),
    # Page for editing an existing blog.
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    # Page for editing a blog post.
    path('edit_blog_post/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
]
