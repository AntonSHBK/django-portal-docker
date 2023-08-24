# -*- coding: utf-8 -*-

from typing import Any

from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views.generic.list import ListView

from blog.models import Post

class UserPostListView(ListView):
    # Сама модель
    model = Post
    # Название шаблона
    template_name = 'blog/user_posts.html'
    # Контекст переменная хранения данных
    context_object_name = 'blog_post_user_list'    
    
    def get_queryset(self) -> QuerySet[Any]:
        user: User = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created') 