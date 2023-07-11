from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from crafthub_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    To retrieve a post and edit or delete it if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
