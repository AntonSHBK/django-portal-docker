# -*- coding: utf-8 -*-

from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.db.models.query import QuerySet
from django.views.generic import (
    TemplateView, 
    ListView,
    )
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    )

# Models
from blog.models import Post

# Forms
from blog.forms import NewPostForm,  NewPostModelForm

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
class NewArticleFormView(FormView):
    # Шаблон
    template_name = 'blog/new_post.html'
    # Форма
    form_class = NewPostForm
    # Redirect url
    success_url =  reverse_lazy('blog:all-authors')
    
    def form_valid(self, form:NewPostForm) -> HttpResponse:
        valid_date = form.cleaned_data
        valid_date['author'] = self.request.user
        save = Post.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    
# About "CreateView" exemple
# https://www.agiliq.com/blog/2019/01/django-createview/
class NewArticleCreateView(CreateView):
    # model = NewPostModelForm
    # fields = ['title',  'content']
  
    def __init__(self, **kwargs: Any) -> None:
        # Шаблон
        self.template_name = 'blog/new_post.html'
        # Форма
        self.form_class = NewPostModelForm
        super(NewArticleCreateView, self).__init__(**kwargs)
    
    # Инициализируем  начальные значения полей формы 
    def get_initial(self, *args, **kwargs):
        """
        Инициализирует начальные значения полей формы
        """
        initial = super(NewArticleCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        initial['content'] = 'My Context'
        return initial
    
    # Добавляем лополниттельные кварги
    def get_form_kwargs(self, *args, **kwargs):
        """
        Возвращает словарь аргументов для экземпляра формы
        """
        kwargs = super(NewArticleCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs
    
    # Валидация формы
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        messages.success(self.request, "The article was created successfully.")
        
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        # instance = form.save(commit=False)

        # Теперь, когда у нас есть несохранённая модель, можно ей чего-нибудь
        # накрутить. Например, заполнить внешний ключ на auth.User. У нас же
        # блог, а не анонимный имижборд, правда?
        # instance.user = self.request.user

        # А теперь можно сохранить в базу
        # instance.save()
        # return redirect(self.get_success_url())
        
        return super(NewArticleCreateView, self).form_valid(form)
    
    # Если форма не валидна
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    
    def get_success_url(self) -> str:
         # Redirect url
        self.success_url =  reverse(
            'blog:one-post',
            args=[self.object.author , self.object.id]
            )
        return super(NewArticleCreateView, self).get_success_url()
        

class EditArticleUpdateView(UpdateView):
    
    # Шаблон
    template_name = 'blog/edit_post.html'
    # Форма
    form_class = NewPostModelForm
    # Модель
    model = Post
    # Redirect url
    success_url =  reverse_lazy('blog:all-authors')
    
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EditArticleUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(EditArticleUpdateView,self).form_valid(form)
    
    def get_success_url(self) -> str:
         # Redirect url
        self.success_url =  reverse(
            'blog:one-post',
            args=[self.object.author , self.object.id]
            )
        return super(EditArticleUpdateView, self).get_success_url()

class DelleteArticleDeleteView(DeleteView):
    
    model = Post
    template_name = 'blog/delet_post.html'
    
    def get_success_url(self) -> str:
         # Redirect url
        self.success_url =  reverse(
            'blog:user-post-list',
            args=[self.request.user]
            )
        return super(DelleteArticleDeleteView, self).get_success_url()


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
    

class OneArticle(TemplateView):   
    model = Post
    template_name = 'blog/one_post.html'
    
    def __init__(self, **kwargs: Any) -> None:
        super(OneArticle, self).__init__(**kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(OneArticle, self).get_context_data(**kwargs)
        context["object"] = get_object_or_404(
            Post, id=self.kwargs.get('post_id'))
        return context
    