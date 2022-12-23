from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:cats>/', views.group_posts)
]