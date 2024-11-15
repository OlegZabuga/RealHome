from rest_framework import generics
from .serializers import ApartmentSerializer, FloorSerializer, BuildingSerializer, ProjectSerializer
from .pagination import ApartmentPagination, FloorPagination
from .repository import ApartmentRepository, FloorRepository, BuildingRepository, ProjectRepository


class ApartmentListAPI(generics.ListCreateAPIView):
    queryset = ApartmentRepository.get_all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination


class FloorListAPI(generics.ListCreateAPIView):
    queryset = FloorRepository.get_all()
    serializer_class = FloorSerializer
    pagination_class = FloorPagination


class BuildingListAPI(generics.ListCreateAPIView):
    queryset = BuildingRepository.get_all()
    serializer_class = BuildingSerializer


class ProjectListAPI(generics.ListCreateAPIView):
    queryset = ProjectRepository.get_all()
    serializer_class = ProjectSerializer