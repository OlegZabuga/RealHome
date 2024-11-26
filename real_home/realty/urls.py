from django.urls import path, include


urlpatterns = [
    path('apartments/', include('realty.domain.apartment.urls')),
    path('floors/', include('realty.domain.floor.urls')),
    path('buildings/', include('realty.domain.building.urls')),
    path('projects/', include('realty.domain.project.urls')),
]