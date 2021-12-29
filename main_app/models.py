from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

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
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  decorations = models.ManyToManyField(Decoration)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fish_detail', kwargs={'fish_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']