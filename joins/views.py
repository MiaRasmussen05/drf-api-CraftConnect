from rest_framework import generics, permissions
from crafthub_api.permissions import IsOwnerOrReadOnly
from joins.models import Join
from joins.serializers import JoinSerializer


class JoinList(generics.ListCreateAPIView):
    """
    List joins or create a join if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = JoinSerializer
    queryset = Join.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JoinDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a join or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = JoinSerializer
    queryset = Join.objects.all()
