from .apartment import Apartment
from .dataclasses import ApartmentData


class ApartmentRepository:
    @staticmethod
    def get_all_apartments():
        apartments = Apartment.objects.select_related('type',
                                                      'floor',
                                                      'section',
                                                      'building').all()
        return [
            ApartmentData(
                id=apartment.id,
                num=apartment.num,
                on_sale=apartment.on_sale,
                type_id=apartment.type.id,
                floor_id=apartment.floor.id,
                section_id=apartment.section.id,
                building_id=apartment.building.id,
                image_url=apartment.image,
            )
            for apartment in apartments
        ]

    @staticmethod
    def get_apartment_by_id(apartment_id):
        try:
            apartment = Apartment.objects.select_related('type',
                                                         'floor',
                                                         'section',
                                                         'building').get(id=apartment_id)
            return ApartmentData(
                id=apartment.id,
                num=apartment.num,
                on_sale=apartment.on_sale,
                type_id=apartment.type.id,
                floor_id=apartment.floor.id,
                section_id=apartment.section.id,
                building_id=apartment.building.id,
                image_url=apartment.image
            )
        except Exception:
            raise ValueError(f'Ошибка! Квартира с id {apartment_id} не существует')

    @staticmethod
    def get_apartments_by_building(building_id):
        apartments = Apartment.objects.select_related('type',
                                                      'floor',
                                                      'section',
                                                      'building').filter(building_id=building_id)
        return [
            ApartmentData(
                id=apartment.id,
                num=apartment.num,
                on_sale=apartment.on_sale,
                type_id=apartment.type.id,
                floor_id=apartment.floor.id,
                section_id=apartment.section.id,
                building_id=apartment.building.id,
                image_url=apartment.image,
            )
            for apartment in apartments
        ]
