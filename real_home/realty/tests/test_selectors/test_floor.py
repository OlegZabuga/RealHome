from django.test import TestCase
from realty.domain.floor.selectors import FloorRepository
from realty.models import Floor, Section


class FloorRepositoryTest(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='1')

        self.floor1 = Floor.objects.create(
            floor_number=1,
            section=self.section,
        )

        self.floor2 = Floor.objects.create(
            floor_number=2,
            section=self.section,
        )

    def test_get_all_floors(self):
        floors = FloorRepository.get_all_floors()
        self.assertEqual(len(floors), 2)

        floors_data = floors[0]
        self.assertEqual(floors_data.id, self.floor1.id)
        self.assertEqual(floors_data.floor_number, self.floor1.floor_number)
        self.assertEqual(floors_data.section_id, self.section.id)

    def test_get_floor_by_id_success(self):
        floor_data = FloorRepository.get_floor_by_id(self.floor1.id)

        self.assertEqual(floor_data.id, self.floor1.id)
        self.assertEqual(floor_data.floor_number, self.floor1.floor_number)
        self.assertEqual(floor_data.section_id, self.section.id)

    def test_get_floor_by_id_fail(self):
        with self.assertRaises(ValueError) as context:
            FloorRepository.get_floor_by_id(10)
        self.assertEqual(str(context.exception), 'Ошибка! Этажа с id 10 не существует')