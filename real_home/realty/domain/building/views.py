from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .selectors import BuildingRepository
from .serializers import BuildingSerializer


class BuildingListView(APIView):
    def get(self, request):
        buildings = BuildingRepository.get_all_buildings()
        paginator = PageNumberPagination()
        paginator.page_size = 3
        paginated_buildings = paginator.paginate_queryset(buildings, request)
        serializer = BuildingSerializer(paginated_buildings, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class BuildingDetailView(APIView):
    def get(self, request, building_id):
        try:
            building = BuildingRepository.get_building_by_id(building_id)
            serializer = BuildingSerializer(building, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
