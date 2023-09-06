# -*- coding: utf-8 -*-

from django.contrib.auth import views
from django.urls import path

app_name = "customer"

urlpatterns = [
    # Autorisation customer
    path('login/', views.LoginView.as_view(), name='login_customer'),
    # Log out customer
    path('logout/', views.LogoutView.as_view(), name='logout_customer'),

]

