from django.shortcuts import render
from django.http import HttpResponse
from fashionpointapp.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
 return render(request, 'fashionpointapp/index.html',)
def categories(request):
 return render(request, 'fashionpointapp/categories.html',)
def show_category(request, category_name_slug):
 context_dict = {}
 try:
  category = Category.objects.get(slug=category_name_slug)
  context_dict['category'] = category
 except Category.DoesNotExist:
  context_dict['category'] = None
 return render(request, 'fashionpointapp/category.html', context_dict)

def contact_us(request):
	return render(request, 'fashionpointapp/contact_us.html',)

def about_us(request):
	return render(request, 'fashionpointapp/about.html',)

def sitemap(request):
	return render(request, 'fashionpointapp/sitemap.html',)

def PostaPost(request):
	return render(request, 'fashionpointapp/PostaPost.html',)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    user = authenticate(username='Anas', password='Anas1234')
    login(request, user)
    return HttpResponseRedirect(reverse('index'))
