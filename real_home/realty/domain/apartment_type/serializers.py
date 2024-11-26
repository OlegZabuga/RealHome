from rest_framework import serializers
from realty.domain import ApartmentType


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = '__all__'