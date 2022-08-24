from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisinformationViewSet.as_view()),
    path('disinformationget', views.DisinformationGetViewSet.as_view()),
    path('user/', views.UserViewSet.as_view()),
    path('userverification/', views.UserVerificationViewSet.as_view()),
    path('usergetdisinformations/', views.UserGetDisinformationsViewSet.as_view()),

]