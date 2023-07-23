from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    id = serializers.ReadOnlyField()
    is_overdue = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_is_overdue(self, obj):
        now = timezone.now()
        if obj.date_of_event < now:
            return True
        else:
            return False

    class Meta:
        model = Event
        fields = [
            'name', 'description', 'owner', 'is_owner', 
            'created_at', 'updated_at', 'start_date_time',
            'end_date_time', 'website_link', 'location', 'cost', 
            'cover_image', 'id', 'is_overdue'
        ]
