from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Apartment, ApartmentType, Floor, Section, Building


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    type = ApartmentTypeSerializer()
    floor = PrimaryKeyRelatedField(queryset=Floor.objects.all())
    section = PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = Apartment
        fields = ['num', 'on_sale', 'type', 'floor', 'section']



class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ['id']