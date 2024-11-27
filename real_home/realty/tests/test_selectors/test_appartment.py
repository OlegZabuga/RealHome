from django.test import TestCase
from realty.domain.apartment.selectors import ApartmentRepository
from realty.models import Apartment, ApartmentType, Floor, Section, Building


class ApartmentRepositoryTest(TestCase):
    def setUp(self):
        self.type = ApartmentType.objects.create(plane='Студия')
        self.floor = Floor.objects.create(floor_number=1)
        self.section = Section.objects.create(name='1')
        self.building = Building.objects.create(num=8)

        self.apartment1 = Apartment.objects.create(
            num=1,
            on_sale=True,
            type=self.type,
            floor=self.floor,
            section=self.section,
            building=self.building,
            image='image1.jpg'
        )

        self.apartment2 = Apartment.objects.create(
            num=2,
            on_sale=True,
            type=self.type,
            floor=self.floor,
            section=self.section,
            building=self.building,
            image='image2.jpg'
        )

    def test_get_all_apartments(self):
        apartments = ApartmentRepository.get_all_apartments()
        self.assertEqual(len(apartments), 2)

        apartment_data = apartments[0]
        self.assertEqual(apartment_data.id, self.apartment1.id)
        self.assertEqual(apartment_data.num, self.apartment1.num)
        self.assertEqual(apartment_data.on_sale, self.apartment1.on_sale)
        self.assertEqual(apartment_data.type_id, self.type.id)
        self.assertEqual(apartment_data.floor_id, self.floor.id)
        self.assertEqual(apartment_data.section_id, self.section.id)
        self.assertEqual(apartment_data.building_id, self.building.id)
        self.assertEqual(apartment_data.image_url, self.apartment1.image)

    def test_get_apartment_by_id_success(self):
        apartment_data = ApartmentRepository.get_apartment_by_id(self.apartment1.id)

        self.assertEqual(apartment_data.id, self.apartment1.id)
        self.assertEqual(apartment_data.num, self.apartment1.num)
        self.assertEqual(apartment_data.on_sale, self.apartment1.on_sale)
        self.assertEqual(apartment_data.type_id, self.type.id)
        self.assertEqual(apartment_data.floor_id, self.floor.id)
        self.assertEqual(apartment_data.section_id, self.section.id)
        self.assertEqual(apartment_data.building_id, self.building.id)
        self.assertEqual(apartment_data.image_url, self.apartment1.image)

    def test_get_apartment_by_id_fail(self):
        with self.assertRaises(ValueError) as context:
            ApartmentRepository.get_apartment_by_id(10)
        self.assertEqual(str(context.exception), "Ошибка! Квартира с id 10 не существует")
