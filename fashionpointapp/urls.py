from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin
from fashionpointapp import views	 
from .views import (
    PostUpdateView,
    PostDeleteView
)
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name="categories"),
    url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.show_post, name='show_post'),
    url(r'^polls/(?P<poll_id>[0-9]+)/$', views.show_poll, name='show_poll'),
    url(r'^updatePosts/$', views.updatePosts, name='updatePosts'),
    url(r'^updatePolls/$', views.updatePolls, name='updatePolls'),
    url(r'^posts/(?P<post_id>[0-9]+)/update_avg/$', views.update_avg, name='update_avg'),
    url(r'^posts/(?P<post_id>[0-9]+)/makeacomment/$', views.makeacomment, name='makeComment'),
    url(r'^polls/(?P<poll_id>[0-9]+)/makeapollcomment/$', views.makeapollcomment, name='makepollComment'),
    url(r'^polls/(?P<poll_id>[0-9]+)/refreshpoll/$', views.update_pollcomments, name='update_pollcomments'),
    url(r'^polls/(?P<poll_id>[0-9]+)/$', views.show_poll, name='show_poll'),
    url(r'^polls/(?P<poll_id>[0-9]+)/click/$', views.click, name='click'),
    url(r'^posts/(?P<post_id>[0-9]+)/refresh/$', views.update_comments, name='update_comments'),
    url(r'^contact/$', views.contact_us, name="contact_us"),
    url(r'^about/$', views.about_us, name="about_us"),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="login"),
	url(r'^signup/$', views.register, name="signup"),
    url(r'^newpost/$', views.Post_form , name="newpost"),
    url(r'^newpoll/$', views.PollaPoll , name="newpoll"),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^posts/(?P<post_id>[0-9]+)/showMore/$', views.showMore, name='showMore'),
    url(r'^polls/(?P<poll_id>[0-9]+)/showMoreP/$', views.showMoreP, name='showMoreP'),
    url(r'^posts/(?P<post_id>[0-9]+)/updateLike/$', views.updateLike, name='updateLike'),
    url(r'^polls/(?P<poll_id>[0-9]+)/updateLikeP/$', views.updateLikeP, name='updateLikeP'),
    url(r'^pic/$', views.edit_pic, name='edit_pic'),
    url(r'^(?P<user_n>[A-Za-z0-9]+)/$', views.view_profile, name='view_profile'),
    url(r'^posts/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^posts/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='Post_Delete'),
]
