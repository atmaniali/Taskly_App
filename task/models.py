from typing import Any
from django.db import models
from django.utils.deconstruct import deconstructible
import uuid
import os

# Create your models here.
NOT_COMPLET = 'NC'
COMPLET = 'C'
TASK_STATUS_CHOICES = (
    (NOT_COMPLET, 'Not Complet'),
    (COMPLET, 'complet')
)


@deconstructible
class GenerateAttachementFilePath(object):
    def __init__(self) -> None:
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'task/{instance.task.id}/attachement/'
        name = f'{instance.id}.{ext}'
        return os.path.join(path, name)


attachementPath = GenerateAttachementFilePath()


class TaskList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)
    house = models.ForeignKey(
        'house.House', on_delete=models.CASCADE, related_name='lists')
    created_by = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, related_name='lists', null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        choices=TASK_STATUS_CHOICES, max_length=2, default=NOT_COMPLET)

    def __str__(self) -> str:
        return f'{self.name} | {self.id}'


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)
    # completed_on = models.DateTimeField(blank=True, null=True)
    completed_by = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, related_name='completed_tasks', null=True, blank=True)
    created_by = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, related_name='created_tasks', null=True, blank=True)
    task_list = models.ForeignKey(
        'task.TaskList', on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        choices=TASK_STATUS_CHOICES, max_length=2, default=NOT_COMPLET)

    def __str__(self) -> str:
        return f'{self.name} | {self.id}'


class Attachement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(
        'task.Task', on_delete=models.CASCADE, related_name='attachement')
    data = models.FileField(upload_to=attachementPath)

    def __str__(self) -> str:
        return f"{self.id} | {self.task}"
