from django.urls import path
from . import views

urlpatterns = [
    path('browse/', views.members, name='members'),
]
