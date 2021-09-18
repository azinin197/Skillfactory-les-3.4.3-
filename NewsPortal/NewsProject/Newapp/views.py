from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment
from django.contrib.auth.models import User
from datetime import *


class PostView(ListView):
    model = Post
    template_name = 'postlist.html'
    context_object_name = 'postlist'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['value1'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'