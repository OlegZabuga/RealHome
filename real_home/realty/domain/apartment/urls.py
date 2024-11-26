from django.urls import path

from .views import ApartmentListAPI


urlpatterns = [
    path('', ApartmentListAPI.as_view(), name='apartment-list'),
]