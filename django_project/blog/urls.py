# -*- coding: utf-8 -*-

from django.urls import path
from django.conf import settings

from blog.views import UserPostListView

app_name = "blog"

urlpatterns = [
    path('blog/user/<str:username>/', UserPostListView.as_view(), name='user-post-list')
]

