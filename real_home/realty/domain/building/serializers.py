from rest_framework import serializers

from realty.domain import Building
from realty.domain.project.serializers import ProjectSerializer


class BuildingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Building
        fields = '__all__'
