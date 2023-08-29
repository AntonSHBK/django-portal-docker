# -*- coding: utf-8 -*-

from django.urls import path, re_path
from django.conf import settings
from django.views.generic import TemplateView

from blog.views import UserPostListView

app_name = "blog"

urlpatterns = [
    path('blog/user/<str:username>/', UserPostListView.as_view(), name='user-post-list'),   
    
]

