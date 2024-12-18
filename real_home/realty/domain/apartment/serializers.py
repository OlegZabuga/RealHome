from django.templatetags.static import static
from rest_framework import serializers
from django.conf import settings


class ApartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    num = serializers.IntegerField()
    on_sale = serializers.BooleanField()
    type_id = serializers.IntegerField()
    floor_id = serializers.IntegerField()
    section_id = serializers.IntegerField()
    building_id = serializers.IntegerField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        image_url = getattr(obj, 'image_url', None) or obj.get('image_url')
        if image_url:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(f'{settings.MEDIA_URL}{image_url}')
            return static(image_url)
        return None


