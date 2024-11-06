from rest_framework import generics, pagination
from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentPagination(pagination.PageNumberPagination):
    page_size = 5


class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination
