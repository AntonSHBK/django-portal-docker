# -*- coding: utf-8 -*-

from django.urls import path, re_path
from django.conf import settings
from django.views.generic import TemplateView

from blog.views import (UserPostListView,
                        NewArticleCreateView,
                        NewArticleFormView,
                        AllAuthorsListView)

app_name = "blog"

urlpatterns = [
    # Show all posts user
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post-list'),
    # Create new post 
    path('new_form/', NewArticleFormView.as_view(), name='new-post-form'),
    path('new/', NewArticleCreateView.as_view(), name='new-post'),

    path('edit/post/<int:post_id>', NewArticleFormView.as_view(), name='new-post'),
    path('del/post/<int:post_id>', NewArticleFormView.as_view(), name='new-post'),
    path('all_authors/', AllAuthorsListView.as_view(), name='all-authors'),
]

