from rest_framework import serializers
from django.templatetags.static import static
from django.conf import settings


class BuildingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    num = serializers.IntegerField()
    on_street = serializers.CharField()
    project_id = serializers.IntegerField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        image_url = getattr(obj, 'image_url', None) or obj.get('image_url')
        if image_url:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(f'{settings.MEDIA_URL}{image_url}')
            return static(image_url)
        return None