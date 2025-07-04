from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed

def index(request):
    return HttpResponse("Cats app is working!")

# Cat Views
class CatList(ListView):
    model = Cat
    template_name = 'cats/cat_list.html'
    context_object_name = 'cat_list'

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('all')

class CatUpdate(UpdateView):
    model = Cat
    fields = '__all__'
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('all')

class CatDelete(DeleteView):
    model = Cat
    template_name = 'cats/cat_confirm_delete.html'
    success_url = reverse_lazy('all')

# Breed Views
class BreedList(ListView):
    model = Breed
    template_name = 'cats/breed_list.html'
    context_object_name = 'breed_list'

class BreedCreate(CreateView):
    model = Breed
    fields = '__all__'
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('breed_list')

class BreedUpdate(UpdateView):
    model = Breed
    fields = '__all__'
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('breed_list')

class BreedDelete(DeleteView):
    model = Breed
    template_name = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('breed_list') 