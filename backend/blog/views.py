# -*- coding: utf-8 -*-


from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views.generic.list import ListView

from blog.models import Post

class UserPostMixin():
    # выборка мользователя: всё то что написано ниже т.е.
    # user: User = get_object_or_404(User, username=self.kwargs.get('username'))
    # можно описать здесь
    pass

class UserPostFormMixin():
    # Миксин для форм
    # model = Post
    # fields = ['title', 'content']
    # succes_url_reddirect = revers_lazy('exemple')
    pass

class UserPostListView(ListView):
    # Сама модель
    model = Post
    # Название шаблона
    template_name = 'blog/user_posts.html'
    # Контекст переменная хранения данных
    
    def get_context_data(self, **kwargs):
        user: User = get_object_or_404(User, username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        queryset = Post.objects.filter(author=user)
        context["blog_post_user_list"] = queryset.order_by('date_created')
        return context
    
    # context_object_name = 'blog_post_user_list'    
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     user: User = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created') 