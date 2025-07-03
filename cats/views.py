from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cat, Breed
from django.urls import reverse_lazy

# Create your views here.

class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = "cats/cat_list.html"

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cat_list')
    template_name = 'cats/cat_form.html'

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cat_list')
    template_name = 'cats/cat_form.html'

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cat_list')
    template_name = 'cats/cat_confirm_delete.html'

class BreedList(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html'

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('breed_list')
    template_name = 'cats/breed_form.html'

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('breed_list')
    template_name = 'cats/breed_form.html'

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('breed_list')
    template_name = 'cats/breed_confirm_delete.html'
