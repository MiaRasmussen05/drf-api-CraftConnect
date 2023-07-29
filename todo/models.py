from django.db import models
from django.contrib.auth.models import User


class Idea(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TaskCategory(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, related_name='todo_items', on_delete=models.CASCADE, null=True,)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(TaskCategory, blank=True, null=True, on_delete=models.SET_NULL)
    completed_percentage = models.IntegerField(default=0)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TaskContent(models.Model):
    task = models.ForeignKey(Task, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField()