from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(requests):
    """
    Create a view that will return a list
    
