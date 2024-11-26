from rest_framework import generics

from realty.domain.building.serializers import BuildingSerializer
from realty.repository import BuildingRepository


class BuildingListAPI(generics.ListCreateAPIView):
    queryset = BuildingRepository.get_all()
    serializer_class = BuildingSerializer