from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .selectors import FloorRepository
from .serializers import FloorSerializer


class FloorListView(APIView):
    def get(self, request):
        floors = FloorRepository.get_all_floors()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_floors = paginator.paginate_queryset(floors, request)
        serializer = FloorSerializer(paginated_floors, many=True)
        return paginator.get_paginated_response(serializer.data)


class FloorDetailView(APIView):
    def get(self, request, floor_id):
        try:
            floor = FloorRepository.get_floor_by_id(floor_id)
            serializer = FloorSerializer(floor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)