from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    # This deals with creating a user_profile for every user that is created in the system through signals
    if created:
        UserProfile.objects.create(user=instance)
