from .domain import Apartment, Floor, Building, Project


class ApartmentRepository:
    @staticmethod
    def get_all():
        return Apartment.objects.all()



class FloorRepository:
    @staticmethod
    def get_all():
        return Floor.objects.all()


class BuildingRepository:
    @staticmethod
    def get_all():
        return Building.objects.all()


class ProjectRepository:
    @staticmethod
    def get_all():
        return Project.objects.all()