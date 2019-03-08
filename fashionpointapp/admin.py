from django.contrib import admin
from fashionpointapp.models import Category, Post, Poll, PostComment, PollComment, Rating, Vote, UserProfile
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Poll)
admin.site.register(PostComment)
admin.site.register(PollComment)
admin.site.register(Rating)
admin.site.register(Vote)
