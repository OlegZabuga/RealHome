from django.urls import path

from .views import FloorListAPI


urlpatterns = [
    path('', FloorListAPI.as_view(), name='floor-list'),
]