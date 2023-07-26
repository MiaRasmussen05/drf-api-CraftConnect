from django.db import IntegrityError
from rest_framework import serializers
from .models import Join


class JoinSerializer(serializers.ModelSerializer):
    """
    Serializer for the Join model
    The create method handles the unique constraint on 'owner' and 'event'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Join
        fields = [
            'id', 'owner', 'created_at', 'event'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
