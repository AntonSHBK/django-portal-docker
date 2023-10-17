# -*- coding: utf-8 -*-

from django.urls import path, re_path
from django.conf import settings
from django.views.generic import TemplateView

from blog.views import (UserPostListView,
                        OneArticle,
                        NewArticleCreateView,
                        NewArticleFormView,
                        AllAuthorsListView,
                        EditArticleUpdateView,
                        DelleteArticleDeleteView)

app_name = "blog"

urlpatterns = [
    # Show all posts user
    path('user/', AllAuthorsListView.as_view(), name='all-authors'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post-list'),
    path('user/<str:username>/post/<int:post_id>', OneArticle.as_view(), name='one-post'),
    # Create new post 
    path('new_form/', NewArticleFormView.as_view(), name='new-post-form'),
    path('new/', NewArticleCreateView.as_view(), name='new-post'),

    path('edit/post/<int:pk>', EditArticleUpdateView.as_view(), name='edit-post'),
    path('del/post/<int:pk>', DelleteArticleDeleteView.as_view(), name='delete-post'),
    
]

