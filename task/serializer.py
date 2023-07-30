from rest_framework import serializers

from .models import TaskList, Task, Attachement
from house.models import House


NOT_COMPLET = 'NC'
COMPLET = 'C'
TASK_STATUS_CHOICES = (
    (NOT_COMPLET, 'Not Complet'),
    (COMPLET, 'complet')
)


class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(
        read_only=True, many=False, view_name='profile-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'house', 'created_on', 'completed_on',
                  'created_by', 'description', 'status', 'name']
        read_only_fields = ['created_on', 'completed_on', 'status']


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    task_list= serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False, view_name='tasklist-detail')
    class Meta:
        model = Task
        fields = ['url', 'id', 'created_on', 'created_on', 'completed_by', 'created_by', 'task_list', 'name', 'description', 'status']
        read_only_fields = ['completed_on', 'created_on', 'completed_by', 'created_by']


class AttachementSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name='task-detail')
    class Meta:
        model = Attachement
        fields = ['url', 'id', 'created_on', 'data', 'task']
