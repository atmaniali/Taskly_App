import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

# https://docs.djangoproject.com/en/4.2/topics/migrations/#migration-serializing
# django serialize migration


@deconstructible
class GenerateImageProfilePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        path = f"media/account/{instance.user.id}/images/"
        name = f"profile_image.{ext}"
        return os.path.join(path, name)


user_profile_image = GenerateImageProfilePath()

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to=user_profile_image, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}\'s Profile."
