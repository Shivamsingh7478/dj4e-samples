from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('tutorial01/', views.tutorial01_index, name='tutorial01_index'),
]
