import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fashionpoint.settings')

import django
django.setup()

from fashionpointapp.models import Category, Post, Poll, UserProfile
from django.contrib.auth.models import User

from datetime import date
from datetime import datetime
import random

def populate():

	cats = [
			{"name": "Winter",
			 "photo": "/cats/winter.jpg"},
			{"name": "Summer",
			 "photo": "/cats/summer.jpg"},
			{"name": "Spring",
			 "photo": "/cats/spring.jpg"},
			]

	for cat in cats:
		add_cat(cat["name"], cat["photo"])

	u1 = add_userProfile("JohnSnow", "John", "/profile_images/hqRMHITj_400x400.jpg", "Ahmad1234", "John@snow.com")
	u2 = add_userProfile("DaeneryesTarg", "Daeneryes", "/profile_images/Daenerys-Targaryen-7x03-The-Queen-s-Justice-daenerys-targaryen-40617732-2995-4500.jpg", "Ahamd1234", "Daeneryes@stormborn.com")
	c = add_cat("fall", "/cats/fall.jpg")

	add_post(86, u1, c, "the north remembers", "/posts/Arya-Stark.jpg")
	add_post(85, u2, c, "edinburgh tourism", "/posts/sawiss.jpg")
	add_post(84, u1, c, "SSE hydro", "/posts/51708350_2268310323440343_2510689292553027584_n_eIi9ZmN.jpg")

	add_poll(87, u1, c, "the north remembers", "/posts/Arya-Stark.jpg", "/posts/Daenerys-Targaryen-7x03-The-Queen-s-Justice-daenerys-targaryen-40617732-2995-4500_fiw7pYp.jpg")
	add_poll(88, u2, c, "which lanister?", "/posts/download_1.jpg", "/posts/Jaime-Lannister.jpg")

def add_cat(name,picture):
	c = Category.objects.get_or_create(name=name)[0]
	c.picture = picture
	c.save()
	return c

def add_userProfile(name, firstname, picture, password, email):
	u = User.objects.create_user(name, email, password)
	u.first_name = firstname
	u.save()
	up = UserProfile.objects.get_or_create(user=u)[0]
	up.dateOfBirth = date.today()
	up.picture = picture
	up.save()
	return up

def add_post(id, userPofile, category, description, photo):
	p = Post(id=id)
	p.userPofile = userPofile
	p.category.add(category)
	p.description = description
	p.avgRating = 0
	p.date = date.today()
	p.photo = photo
	p.save()
	return p

def add_poll(id, userPofile, category, description, picture1, picture2):
	p = Poll(id=id)
	p.userPofile = userPofile
	p.category.add(category)
	p.description = description
	p.date = date.today()
	p.picture1 = picture1
	p.picture2 = picture2
	p.picture1Clicks = 0
	p.picture2Clicks = 0
	p.save()
	return p

# Start execution here!
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
