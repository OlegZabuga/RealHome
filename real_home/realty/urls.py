from .views import ApartmentListAPI, FloorListAPI
from django.urls import path


urlpatterns = [
    path('apartments/', ApartmentListAPI.as_view(), name='apartment-list'),
    path('floors/', FloorListAPI.as_view(), name='floor-list'),
]