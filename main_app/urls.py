from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fish/', views.fish_index, name='fish_index'),
  path('fish/<int:fish_id>/', views.fish_detail, name='fish_detail'),
  path('fish/create/', views.FishCreate.as_view(), name='fish_create')
]