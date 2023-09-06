# -*- coding: utf-8 -*-

from django.urls import path

from .views import MainPageView

urlpatterns = [
    # Main page (Home page)
    path('', MainPageView.as_view(), name='main_page'),
]

