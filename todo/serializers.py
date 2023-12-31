from django.db import IntegrityError
from rest_framework import serializers
from .models import Idea, TaskCategory, Task, Todo, TaskContent


class IdeaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Idea
        fields = [
            'owner', 'is_owner', 'created_at',
            'id', 'title', 'description'
        ]


class TaskCategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = TaskCategory
        fields = [
            'id', 'name', 'owner', 'is_owner'
            ]


class TaskContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskContent
        fields = ['id', 'content']


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    contents = TaskContentSerializer(many=True, read_only=True)
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'idea', 'owner', 'is_owner',
            'title', 'content', 'created_at', 'category',
            'completed_percentage', 'completed', 'contents'
        ]


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Todo
        fields = [
            'owner', 'is_owner', 'created_at',
            'id', 'title'
        ]