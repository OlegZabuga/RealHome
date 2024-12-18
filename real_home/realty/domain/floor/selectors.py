from .dataclasses import FloorData
from realty.models.floor import Floor


class FloorRepository:
    @staticmethod
    def get_all_floors():
        floors = Floor.objects.select_related('section').all()
        return [
            FloorData(
                id=floor.id,
                floor_number=floor.floor_number,
                section_id=floor.section.id,
            )
            for floor in floors
        ]

    @staticmethod
    def get_floor_by_id(floor_id):
        try:
            floor = Floor.objects.select_related('section').get(id=floor_id)
            return FloorData(
                id=floor.id,
                floor_number=floor.floor_number,
                section_id=floor.section.id,
            )
        except Exception:
            raise ValueError(f'Ошибка! Этажа с id {floor_id} не существует')