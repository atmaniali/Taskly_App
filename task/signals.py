from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Task, COMPLET, NOT_COMPLET


@receiver(post_save, sender=Task)
def update_house_point(sender, instance, created, **kwargs):
    house = instance.task_list.house
    if instance.status == COMPLET:
        house.point += 10
    elif instance.status == NOT_COMPLET:
        if house.point > 10:
            house.point -= 10

    house.save()


@receiver(pre_save, sender=Task)
def update_task_list_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_completed = True
    for task in task_list.lists.all():
        if task.status == NOT_COMPLET:
            is_completed = False
            break

    task_list.status = COMPLET if is_completed else NOT_COMPLET
    task_list.save()
