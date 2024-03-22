"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myCV import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('user_details',views.user_details,name='user_details'),
    path('accept',views.accept,name='accept'),
    path('resume',views.resume,name='resume'),
    path('res',views.res,name='res'),
    path('list',views.list,name='list'),
    path('list_download',views.list_download,name='list_download'),
    path('faq',views.faq,name='faq'),
    path('user_data',views.user_data,name='user_data'),
    path('check',views.check,name='check'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about_us',views.about_us,name='about_us'),
]