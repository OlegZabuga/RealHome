from rest_framework import serializers


class FloorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    floor_number = serializers.IntegerField()
    section_id = serializers.IntegerField()