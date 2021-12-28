from django.db import models
from django.urls import reverse

# Create your models here.
class Decoration(models.Model):
  name = models.CharField(max_length=40)
  color = models.CharField(max_length=20)
  description = models.CharField(max_length=300)
  price = models.IntegerField()

class Fish(models.Model):
  name = models.CharField(max_length=40)
  species = models.CharField(max_length=40)
  color = models.CharField(max_length=20)
  price = models.IntegerField()
  age = models.IntegerField()
  # decorations = models.ManyToManyField(Decoration)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fish_detail', kwargs={'fish_id': self.id})