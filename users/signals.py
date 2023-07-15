from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ this function wil create new profile automaticly every time new User has created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    username = f"{instance.first_name}_{instance.last_name}"
    counter = 1

    while User.objects.filter(username=username):
        username = f"{instance.first_name}_{instance.last_name}_{counter}"
        counter += 1

    instance.username = username
