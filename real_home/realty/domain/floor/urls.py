from django.urls import path

from .views import FloorListView, FloorDetailView


urlpatterns = [
    path('', FloorListView.as_view()),
    path('<int:floor_id>/', FloorDetailView.as_view()),
]