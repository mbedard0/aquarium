from django.shortcuts import render
from django.http import HttpResponse
from .models import Fish, Decoration

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.all()
  return render(request, 'fish/index.html', { 'fishes': fish })