from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['url', 'id', 'name', 'image', 'created_at', 'manager', 'description', 'point',
                  'completed_task_count', 'not_completed_task_count', 'members', 'members_count']
        read_only_fields = ['completed_task_count',
                            'not_completed_task_count', 'point']
