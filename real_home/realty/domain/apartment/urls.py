from django.urls import path

from .views import ApartmentListView, ApartmentDetailView


urlpatterns = [
    path('', ApartmentListView.as_view()),
    path('<int:apartment_id>/', ApartmentDetailView.as_view()),
]