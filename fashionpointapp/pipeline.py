from .models import UserProfile
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def save_profile(backend, user, response, *args, **kwargs):
	print(response)

	if(User.objects.filter(username=response['name']) == None):
		u = User.objects.create_user(response['name'], response['email'])
		u.first_name = response['name'].split(' ',1)[0]
		u.save()
		up, ifCreated = UserProfile.objects.get_or_create(user=u)[0]
		up.dateOfBirth = date.today()
		up.picture = "/profile_imsages/default.jpg"
		up.save()
	else:
		print("already user")
		#login(user)
		#return HttpResponseRedirect(reverse('index'))
