from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
] 