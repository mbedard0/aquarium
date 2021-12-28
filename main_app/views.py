from django.shortcuts import render
from django.http import HttpResponse
from .models import Fish, Decoration
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fish/index.html', { 'fishes': fishes })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fish/detail.html', { 'fish': fish})

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'
  # fields = ['name', 'species', 'color', 'price', 'age']
  success_url = '/fish/'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['color', 'price', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'