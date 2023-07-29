import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible
# The `deconstructible` decorator is used in this code to make
# the `GenerateHousePath` class serializable. When a model is
# serialized, Django needs to be able to recreate the object from
# the serialized data. By using the `deconstructible` decorator,
# Django knows how to deconstruct and reconstruct the object. In
# this case, it allows Django to properly serialize and
# deserialize the `GenerateHousePath` object when the model is
# migrated or serialized.


# Create your models here.


@deconstructible
class GenerateHousePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"house/{instance.id}/images"
        name = f"house_image.{ext}"
        return os.path.join(path, name)


house_image = GenerateHousePath()


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    image = models.FileField(upload_to=house_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    manager = models.OneToOneField(
        'users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='manage_house')
    point = models.IntegerField(default=0)
    compelted_task_count = models.IntegerField(default=0)
    not_compelted_task_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
