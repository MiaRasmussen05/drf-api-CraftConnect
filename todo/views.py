from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Idea, TaskCategory, Task
from .serializers import IdeaSerializer, TaskCategorySerializer, TaskSerializer
from crafthub_api.permissions import IsOwnerOrReadOnly


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class TaskCategoryList(generics.ListCreateAPIView):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
    permission_classes = permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]

    def get_queryset(self):
        return Task.objects.filter(idea__owner=self.request.user)

    def perform_create(self, serializer):
        idea = Idea.objects.get(owner=self.request.user)
        serializer.save(idea=idea)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer