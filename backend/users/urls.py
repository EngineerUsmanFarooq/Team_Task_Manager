from django.urls import path
from .views import register, user_login, create_admin

urlpatterns = [
    path("register/", register),
    path("login/", user_login),
    path("setup-admin/", create_admin),
]
