from rest_framework import serializers

from realty.domain import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'