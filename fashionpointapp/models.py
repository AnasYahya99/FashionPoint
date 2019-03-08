from django.db import models
from datetime import date

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	def __str__(self):
		return self.name
class Post(models.Model):
	category = models.ManyToManyField(Category)
	rating = models.FloatField(default=0)
	date = models.DateField(("Date"), default=date.today)
	def __str__(self): 
		return self.id

