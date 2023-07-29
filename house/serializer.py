from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only=True)
    members = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='profile-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True,
                                                  many=False, view_name='profile-detail')

    class Meta:
        model = House
        fields = ['url', 'id', 'name', 'image', 'created_at', 'manager', 'description', 'point',
                  'compelted_task_count', 'not_compelted_task_count', 'members', 'members_count']
        read_only_fields = ['compelted_task_count',
                            'not_compelted_task_count', 'point']
