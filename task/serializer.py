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
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='task-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'house', 'created_on', 'completed_on',
                  'created_by', 'description', 'status', 'name', 'tasks']
        read_only_fields = ['created_on', 'completed_on', 'status']


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False, view_name='tasklist-detail')
    attachement = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='attachement-detail')

    # overide validate data for field task_list to accept only task list in house
    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile
        if value not in user_profile.house.lists.all():
            raise serializers.ValidationError('Task list provided does not belong to house for which profile is member')
        return value

    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task = Task.objects.create(**validated_data)
        task.created_by = user_profile
        task.save()
        return task

    class Meta:
        model = Task
        fields = ['url', 'id', 'created_on', 'created_on', 'completed_by', 'created_by', 'task_list', 'name', 'description', 'status', 'attachement']
        read_only_fields = ['completed_on', 'created_on', 'completed_by', 'created_by', 'status']


class AttachementSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name='task-detail')

    def validate(self, attrs):
        user_profile = self.context['request'].user.profile
        task = attrs['task']
        task_list = TaskList.objects.get(tasks__id__exact=task.id)
        if task_list not in user_profile.house.lists.all():
            raise serializers.ValidationError(
                {'task': 'Task list provided does not belong to house for which profile is member'})
        return attrs
    class Meta:
        model = Attachement
        fields = ['url', 'id', 'created_on', 'data', 'task']
