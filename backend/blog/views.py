# -*- coding: utf-8 -*-

from typing import Any
from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

# Models
from blog.models import Post

# Forms
from blog.forms import NewPost, NewPost_2

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


# About "FormView" exemple
# https://www.agiliq.com/blog/2019/01/django-formview/
class NewArticleView(FormView):
    # Шаблон
    template_name = 'blog/new_post.html'
    # Форма
    form_class = NewPost
    # Redirect url
    success_url =  reverse_lazy('blog:all-authors')
    
    def form_valid(self, form:NewPost) -> HttpResponse:
        valid_date = form.cleaned_data
        save = None
        return super().form_valid(form)
    
    
# About "CreateView" exemple
# https://www.agiliq.com/blog/2019/01/django-createview/
class NewArticleView(CreateView):
    # model = NewPost
    # fields = ['title',  'contennt']

    # Шаблон
    template_name = 'blog/new_post.html'
    # Форма
    form_class = NewPost_2
    # Redirect url
    success_url =  reverse_lazy('blog:all-authors')
    
    # def form_valid(self, form) -> HttpResponse:
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    
    # def get_initial(self, *args, **kwargs):
    #     initial = super(BookCreateView, self).get_initial(**kwargs)
    #     initial['title'] = 'My Title'
    #     return initial
    
    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(BookCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['user'] = self.request.user
    #     return kwargs
    

# About "ListView" exemple
# https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/
class AllAuthorsListView(ListView):
    # Сама модель
    model = User
    # Название шаблона
    template_name = 'blog/all_authors.html'
    # Контекст переменная хранения данных
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.all()
        context["all_authors"] = queryset
        return context
    
    