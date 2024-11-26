from rest_framework import serializers
from realty.domain import Apartment
from realty.domain.apartment_type.serializers import ApartmentTypeSerializer
from realty.domain.building.serializers import BuildingSerializer
from realty.domain.floor.serializers import FloorSerializer
from realty.domain.section.serializers import SectionSerializer


class ApartmentSerializer(serializers.ModelSerializer):
    type = ApartmentTypeSerializer()
    floor = FloorSerializer()
    section = SectionSerializer()
    building = BuildingSerializer()


    class Meta:
        model = Apartment
        fields = ['num', 'building', 'on_sale', 'type', 'floor', 'section', 'image']