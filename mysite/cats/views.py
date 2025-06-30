from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed

# Create your views here.

class CatList(ListView):
    model = Cat
    template_name = "cats/cat_list.html"

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')

class BreedList(ListView):
    model = Breed
    template_name = "cats/breed_list.html"

class BreedCreate(CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedUpdate(UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:breed_list')
