from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import ProjectSerializer
from .selectors import ProjectRepository


class ProjectListView(APIView):
    def get(self, request):
        projects = ProjectRepository.get_all_projects()
        paginator = PageNumberPagination()
        paginator.page_size = 3
        paginated_projects = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(paginated_projects, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class ProjectDetailView(APIView):
    def get(self, request, project_id):
        try:
            project = ProjectRepository.get_project_by_id(project_id)
            serializer = ProjectSerializer(project, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)