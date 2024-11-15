from django.contrib import admin
from .models import Apartment, ApartmentType, Floor, Section, Building, Project
from .forms import ApartmentForm, ApartmentTypeForm, FloorForm, SectionForm, BuildingForm, ProjectForm


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    form = ApartmentForm
    list_display = ('num', 'building', 'image_tag')
    readonly_fields = ('image_tag',)


@admin.register(ApartmentType)
class ApartmentTypeAdmin(admin.ModelAdmin):
    form = ApartmentTypeForm


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    form = FloorForm


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionForm


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    form = BuildingForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
