from django.contrib import admin
from django_simple_forum.models import MainSection, Section, Thread, Post
from django_simple_forum.user_profile.models import UserProfile


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(MainSection)
admin.site.register(Section)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(UserProfile)