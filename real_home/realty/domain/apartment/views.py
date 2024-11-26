from rest_framework import generics

from realty.domain.apartment.serializers import ApartmentSerializer
from realty.pagination import ApartmentPagination
from realty.repository import ApartmentRepository


class ApartmentListAPI(generics.ListCreateAPIView):
    queryset = ApartmentRepository.get_all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination
