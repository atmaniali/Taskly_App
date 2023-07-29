from rest_framework import serializers

from .models import TaskList
from house.models import House


NOT_COMPLET = 'NC'
COMPLET = 'C'
TASK_STATUS_CHOICES = (
    (NOT_COMPLET, 'Not Complet'),
    (COMPLET, 'complet')
)


class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(
        many=True, queryset=House.objects.all(), name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(
        read_only=True, many=False, view_name='profile-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'house', 'created_on', 'completed_on',
                  'created_by', 'description', 'status', 'name']
        read_only_fields = ['created_on', 'completed_on', 'status']
