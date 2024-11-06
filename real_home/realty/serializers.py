from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Apartment, Floor


class ApartmentSerializer(serializers.ModelSerializer):
    floor = PrimaryKeyRelatedField(queryset=Floor.objects.all())

    class Meta:
        model = Apartment
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ['id']