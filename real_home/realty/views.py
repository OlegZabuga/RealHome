from rest_framework import generics
from .models import Apartment, Floor, Building, Project
from .serializers import ApartmentSerializer, FloorSerializer, BuildingSerializer, ProjectSerializer
from.pagination import ApartmentPagination, FloorPagination


class ApartmentListAPI(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination


class FloorListAPI(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    pagination_class = FloorPagination


class BuildingListAPI(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class ProjectListAPI(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer