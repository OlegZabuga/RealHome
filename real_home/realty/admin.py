from django.contrib import admin
from .models import Apartment, ApartmentType, Floor, Section, Building, Project


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'on_sale',
        'building',
        'image_tag'
    )
    search_fields = ('num',)
    list_editable = ('on_sale',)
    readonly_fields = ('image_tag',)
    list_filter = ('type', 'on_sale',)


@admin.register(ApartmentType)
class ApartmentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'plane',
        'rooms',
    )
    list_filter = ('rooms',)
    search_fields = ('rooms',)

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = (
        'floor_number',
        'section',
    )
    search_fields = ('floor_number',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'building'
    )
    search_fields = ('building',)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'on_street',
        'project',
        'image_tag'
    )
    readonly_fields = ('image_tag',)
    search_fields = ('num',)
    list_filter = ('project',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount_floors',
        'rating',
        'image_tag'
    )
    search_fields = ('rating', 'amount_floors')
    readonly_fields = ('image_tag',)
    list_filter = ('rating', 'amount_floors')
