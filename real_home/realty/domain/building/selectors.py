from .dataclasses import BuildingData
from .building import Building


class BuildingRepository:
    @staticmethod
    def get_all_buildings():
        buildings = Building.objects.select_related('project').all()
        return [
            BuildingData(
                id=building.id,
                num=building.num,
                on_street=building.on_street,
                project_id=building.project.id,
                image_url=building.image,
            )
            for building in buildings
        ]

    @staticmethod
    def get_building_by_id(building_id):
        try:
            building = Building.objects.select_related('project').get(id=building_id)
            return BuildingData(
                id=building.id,
                num=building.num,
                on_street=building.on_street,
                project_id=building.project.id,
                image_url=building.image,
            )
        except Exception:
            raise ValueError(f'Ошибка! Корпус с id {building_id} не существует')