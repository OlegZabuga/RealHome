from django.urls import path

from .views import BuildingListAPI


urlpatterns = [
    path('', BuildingListAPI.as_view(), name='building-list'),
]