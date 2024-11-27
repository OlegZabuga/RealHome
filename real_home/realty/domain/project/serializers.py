from rest_framework import serializers
from django.templatetags.static import static
from django.conf import settings


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    amount_floors = serializers.IntegerField()
    rating = serializers.CharField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        image_url = getattr(obj, 'image_url', None) or obj.get('image_url')
        if image_url:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(f'{settings.MEDIA_URL}{image_url}')
            return static(image_url)
        return None