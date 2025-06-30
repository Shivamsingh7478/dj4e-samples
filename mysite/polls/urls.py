from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),  <- We will add this back in a future assignment
    path('owner', views.owner, name='owner'),
] 