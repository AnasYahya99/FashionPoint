from django.contrib import admin
from fashionpointapp.models import Category, Post, Poll, PostComment, PollComment, Rating, Vote, UserProfile,Like,LikePoll
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(UserProfile)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)
admin.site.register(Poll)
admin.site.register(PostComment)
admin.site.register(PollComment)
admin.site.register(Rating)
admin.site.register(Vote)
admin.site.register(Like)
admin.site.register(LikePoll)
