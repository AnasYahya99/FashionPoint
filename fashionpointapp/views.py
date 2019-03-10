from django.shortcuts import render
from django.http import HttpResponse
from fashionpointapp.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'fashionpointapp/index.html', )
