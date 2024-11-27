from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import ApartmentSerializer
from .selectors import ApartmentRepository


class ApartmentListView(APIView):
    def get(self, request):
        apartments = ApartmentRepository.get_all_apartments()
        paginator = PageNumberPagination()
        paginator.page_size = 3
        paginated_apartments = paginator.paginate_queryset(apartments, request)
        serializer = ApartmentSerializer(paginated_apartments, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class ApartmentDetailView(APIView):
    def get(self, request, apartment_id):
        try:
            apartment = ApartmentRepository.get_apartment_by_id(apartment_id)
            serializer = ApartmentSerializer(apartment, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
