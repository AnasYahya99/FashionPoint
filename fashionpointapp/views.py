from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return render(request, 'fashionpointapp/index.html',)
def categories(request):
 return render(request, 'fashionpointapp/categories.html',)

