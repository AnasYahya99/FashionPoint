from django.conf.urls import url
from django.conf.urls import include 
from django.contrib import admin
from fashionpointapp import views	 

urlpatterns = [
<<<<<<< HEAD
	url(r'^$',views.index , name='index'),
	url(r'^categories/$', views.categories, name="categories"),
=======
    url(r'^$', views.indexReset, name='index'),
    url(r'^categories/$', views.categories, name="categories"),
>>>>>>> 01bcae22bf18263763417be650840d1cc21e5b32
    url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^contact/$', views.contact_us, name="contact_us"),
    url(r'^about/$', views.about_us, name="about_us"),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login"),
	url(r'^signup/$', views.register, name="signup"),
    url(r'^newpost/$', views.PostaPost , name="newpost"),
    url(r'^newpoll/$', views.PollaPoll , name="newpoll"),
<<<<<<< HEAD
	url(r'^myaccount/$', views.view_profile, name='view_profile'),
    	url(r'^edit/$', views.edit_profile, name='edit_profile'),
=======
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^nextPosts/$', views.indexNext, name="indNext"),
    url(r'^previousPosts/$', views.indexPrev, name="indPrev"),
>>>>>>> 01bcae22bf18263763417be650840d1cc21e5b32

]
