from rest_framework import generics
from .models import Apartment, Floor
from .serializers import ApartmentSerializer, FloorSerializer
from.pagination import ApartmentPagination, FloorPagination


class ApartmentListAPI(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination


class FloorListAPI(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    pagination_class = FloorPagination
