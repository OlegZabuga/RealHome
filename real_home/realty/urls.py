from .views import ApartmentList
from django.urls import path


urlpatterns = [
    path('apartments/', ApartmentList.as_view(), name='apartment-list'),
]