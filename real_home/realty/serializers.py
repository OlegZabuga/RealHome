from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Apartment, ApartmentType, Floor, Section, Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    type = ApartmentTypeSerializer()
    floor = FloorSerializer()
    section = SectionSerializer()
    building = BuildingSerializer()


    class Meta:
        model = Apartment
        fields = ['num', 'building', 'on_sale', 'type', 'floor', 'section']
