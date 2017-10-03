from django.contrib.auth.models import User
from django.db import models
import django_simple_forum.models
# Imported this way to avoid circular import


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(verbose_name='Avatar',
                               default='uploads/avatars/default.jpg',
                               upload_to='uploads/avatars/'
    )
    title = models.CharField(verbose_name='Title', max_length=32, default='New user')

    @property
    def get_total_posts(self):
        return django_simple_forum.models.Post.objects.filter(user=self.user).count()

    @property
    def get_username(self):
        return self.user.username

