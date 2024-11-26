from rest_framework import generics

from realty.domain.floor.serializers import FloorSerializer
from realty.pagination import FloorPagination
from realty.repository import FloorRepository


class FloorListAPI(generics.ListCreateAPIView):
    queryset = FloorRepository.get_all()
    serializer_class = FloorSerializer
    pagination_class = FloorPagination