from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.RegisterPage,name='registerpage'),
    path("register/",views.UserRegister,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("logiuser/",views.LoginUser,name="login"),
    
   
]