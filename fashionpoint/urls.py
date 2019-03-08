from django.conf.urls import url
from django.conf.urls import include 
from django.contrib import admin
from fashionpointapp import views	
urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', admin.site.urls),
    url(r'^fashionpoint/', include('fashionpointapp.urls')),
=======
	url(r'^$', views.index, name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^fashionpoint/', include('fashionpointapp.urls')),
>>>>>>> 9248fba15c6c2356a061512c8f20c2dd6f786964
]
