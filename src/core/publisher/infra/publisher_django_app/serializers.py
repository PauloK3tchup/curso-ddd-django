from rest_framework import serializers

class CreatePublisherRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required = False)

class CreatePublisherResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    
class ListPublisherResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required = False)
    is_active = serializers.BooleanField()