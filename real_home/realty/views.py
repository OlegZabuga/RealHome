from rest_framework import generics
from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
