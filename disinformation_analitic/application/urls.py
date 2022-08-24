"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers 
#from books.api import viewsets as booksviewsets
from frontendapi import views
route = routers.DefaultRouter()
#route.register(r'our_site/', views.DisinformationViewSet, basename='our_site')
route.register(r'disinformation/', views.DisinformationViewSet, basename='disinformation')
route.register(r'disinformationget/', views.DisinformationGetViewSet, basename='disinformationget')
route.register(r'user/', views.UserViewSet, basename='user')
route.register(r'userverification/', views.UserVerificationViewSet, basename='userverification')
route.register(r'usergetdisinformations/', views.UserGetDisinformationsViewSet, basename='usergetdisinformations')


urlpatterns = [
    path('api/', include(route.urls)),
    path('', include('temporarypage.urls')),
    path('command/', include('interface_command.urls')),
    path('admin/', admin.site.urls),
]

