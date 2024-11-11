from django.contrib import admin
from .models import Apartment, ApartmentType, Floor, Section, Building, Project
from .forms import ApartmentForm


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    form = ApartmentForm
