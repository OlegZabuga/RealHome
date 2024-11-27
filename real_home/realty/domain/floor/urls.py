from django.urls import path

from .views import FloorListView, FloorDetailView


urlpatterns = [
    path('', FloorListView.as_view(), name='floor-list'),
    path('<int:floor_id>/', FloorDetailView.as_view(), name='floor-detail'),
]