from django.db import models
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	dateOfBirth = models.DateField();
	class Meta: 
		verbose_name_plural = 'Users'
	def __str__(self):
		return self.user.username
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	class Meta: 
		verbose_name_plural = 'Categories'
	def __str__(self):
		return self.name
class Post(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	description = models.CharField(max_length=128,null=True,blank=True)
	avgRating = models.FloatField(default=0)
	date = models.DateTimeField(auto_now=True)
	photo = models.ImageField(upload_to="posts/")
	class Meta: 
		verbose_name_plural = 'Posts'
	def __str__(self):
		stringID = str(self.id)
		return stringID
class Poll(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	description = models.CharField(max_length=128,null=True,blank=True)
	date = models.DateTimeField(auto_now=True)
	picture1 = models.ImageField(upload_to="polls/")
	picture2 = models.ImageField(upload_to="polls/")
	picture1Clicks = models.PositiveIntegerField(default=0)
	picture2Clicks = models.PositiveIntegerField(default=0)
	class Meta: 
		verbose_name_plural = 'Polls'
	def __str__(self):
		stringID = str(self.id)
		return stringID

class PostComment(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.CharField(max_length=256,null=True,blank=True)
	date = models.DateTimeField(auto_now=True)
	class Meta: 
		verbose_name_plural = 'Post Comments'
	def __str__(self):
		stringID = str(self.id)
		return stringID
class PollComment(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	comment = models.CharField(max_length=256,null=True,blank=True)
	date = models.DateTimeField(auto_now=True)
	class Meta: 
		verbose_name_plural = 'Poll Comments'
	def __str__(self):
		stringID = str(self.id)
		return stringID
class Rating(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	rating = models.PositiveIntegerField(default=0)
	class Meta: 
		verbose_name_plural = 'Ratings'
	def __str__(self):
		stringID = str(self.id)
		return stringID
class Vote(models.Model):
	userPofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice = models.BooleanField();
	class Meta: 
		verbose_name_plural = 'Votes'
	def __str__(self):
		stringID = str(self.id)
		return stringID