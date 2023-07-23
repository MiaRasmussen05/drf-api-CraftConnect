from rest_framework import serializers
from django.utils import timezone
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
        if obj.start_date_time < now:
            return True
        else:
            return False
    
    def validate(self, data):
        start_date_time = data.get('start_date_time')
        end_date_time = data.get('end_date_time')

        if start_date_time and end_date_time:
            time_difference = end_date_time - start_date_time
            if time_difference.total_seconds() < 3600: 
                raise serializers.ValidationError('End date and time must be at least 1 hours after the start date and time.')

            if end_date_time < start_date_time:
                raise serializers.ValidationError('End date and time must be after or equal to the start date and time.')

        return data

    class Meta:
        model = Event
        fields = [
            'name', 'description', 'owner', 'is_owner', 
            'created_at', 'updated_at', 'start_date_time',
            'end_date_time', 'website_link', 'location', 'cost', 
            'cover_image', 'id', 'is_overdue'
        ]
