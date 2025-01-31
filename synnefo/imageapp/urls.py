"""synnefo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from imageapp import views

urlpatterns = [
    path("",views.index,name="home"),
    path("add/",views.add_person,name="add person" ),
    path("show/",views.get_all_person,name="get persons" ),
    path("loginUser/",views.loginUser,name="loginUser" ),
    path("logoutUser/",views.logoutUser,name="logoutUser"),
    path("createUser/",views.createUser,name="createUser"),
    path("uploadFile/",views.uploadFile,name="uploadFile"),
    path("image",views.image,name="image"),
    path("about",views.about,name="about")
]


