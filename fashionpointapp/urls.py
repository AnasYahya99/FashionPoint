from django.conf.urls import url
from django.conf.urls import include 
from django.contrib import admin
from fashionpointapp import views	
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name="categories"),
    url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^contact/$', views.contact_us, name="contact_us"),
    url(r'^about/$', views.about_us, name="about_us"),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),

]
