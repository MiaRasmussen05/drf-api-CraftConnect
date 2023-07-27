from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Idea, TaskCategory, Task
from .serializers import IdeaSerializer, TaskCategorySerializer, TaskSerializer
from crafthub_api.permissions import IsOwnerOrReadOnly


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IdeaList(generics.ListCreateAPIView):
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Idea.objects.filter(owner=self.request.user)


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class TaskCategoryList(generics.ListCreateAPIView):
    serializer_class = TaskCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except serializers.ValidationError as e:
            return Response({'detail': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return TaskCategory.objects.filter(owner=self.request.user)


class TaskCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(idea__owner=self.request.user)

    def perform_create(self, serializer):
        idea_id = self.request.data.get('idea')
        idea = None
        if idea_id:
            try:
                idea = Idea.objects.get(owner=self.request.user, id=idea_id)
            except Idea.DoesNotExist:
                raise serializers.ValidationError("Invalid Idea ID or Idea does not belong to the user.")
        serializer.save(owner=self.request.user, idea=idea)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer