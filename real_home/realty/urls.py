from .views import ApartmentListAPI, FloorListAPI, BuildingListAPI, ProjectListAPI
from django.urls import path


urlpatterns = [
    path('apartments/', ApartmentListAPI.as_view(), name='apartment-list'),
    path('floors/', FloorListAPI.as_view(), name='floor-list'),
    path('buildings/', BuildingListAPI.as_view(), name='building-list'),
    path('projects/', ProjectListAPI.as_view(), name='project-list'),
]