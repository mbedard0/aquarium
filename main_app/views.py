from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fish, Decoration
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
  feeding_form = FeedingForm()
  return render(request, 'fish/detail.html', { 'fish': fish, 'feeding_form': feeding_form })

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish_detail', fish_id=fish_id)

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'
  success_url = '/fish/'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['color', 'price', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'

class DecorationCreate(CreateView):
  model = Decoration
  fields = '__all__'
  success_url = '/decorations/'

class DecorationList(ListView):
  model = Decoration

class DecorationDetail(DetailView):
  model = Decoration
