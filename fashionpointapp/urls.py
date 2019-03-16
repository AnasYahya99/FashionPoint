from django.conf.urls import url
from django.conf.urls import include 
from django.contrib import admin
from fashionpointapp import views	 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name="categories"),
    url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.show_post, name='show_post'),
    url(r'^posts/(?P<post_id>[0-9]+)/update_avg/$', views.update_avg, name='update_avg'),
    url(r'^posts/(?P<post_id>[0-9]+)/makeacomment/$', views.makeacomment, name='makeComment'),
    url(r'^posts/(?P<post_id>[0-9]+)/refresh/$', views.update_comments, name='update_comments'),
    url(r'^contact/$', views.contact_us, name="contact_us"),
    url(r'^about/$', views.about_us, name="about_us"),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login"),
	url(r'^signup/$', views.register, name="signup"),
    url(r'^newpost/$', views.PostaPost , name="newpost"),
    url(r'^newpoll/$', views.PollaPoll , name="newpoll"),
	url(r'^myaccount/$', views.view_profile, name='view_profile'),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^updatePosts/$', views.updatePosts, name='updatePosts'),
    url(r'^updatePolls/$', views.updatePolls, name='updatePolls'),

]
