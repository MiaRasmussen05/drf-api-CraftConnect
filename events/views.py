from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Event
from .serializers import EventSerializer
from crafthub_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in.
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Event.objects.annotate(
        joins_count=Count('joins', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'cost', 'location',
        'joins__owner__profile',
    ]
    search_fields = [
        'start_date_time',
        'name', 'location', 'cost'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    To retrieve an event and edit or delete it if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly, 
        permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.annotate(
        joins_count=Count('joins', distinct=True)
    ).order_by('-created_at')
