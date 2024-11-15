from rest_framework import serializers
from .models import Apartment, ApartmentType, Floor, Section, Building, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Building
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
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
        fields = ['num', 'building', 'on_sale', 'type', 'floor', 'section', 'image']
