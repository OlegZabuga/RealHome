from rest_framework import generics

from realty.domain.project.serializers import ProjectSerializer
from realty.repository import ProjectRepository


class ProjectListAPI(generics.ListCreateAPIView):
    queryset = ProjectRepository.get_all()
    serializer_class = ProjectSerializer