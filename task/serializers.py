from rest_framework import serializers
from .models import Task, TaskStatus


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'created', 'description', 'cost']


class TaskStatusSerializer(serializers.ModelSerializer):
    task = serializers.ReadOnlyField(source='task.description')

    class Meta:
        model = TaskStatus
        fields = ['id', 'task', 'created', 'status']