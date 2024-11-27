from django.test import TestCase
from realty.domain.building.selectors import BuildingRepository
from realty.models import Building, Project


class BuildingRepositoryTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name='1', description='1', amount_floors=1, rating='A')

        self.building1 = Building.objects.create(
            num=1,
            on_street='Kirova',
            project=self.project,
            image='image.jpg',
        )

        self.building2 = Building.objects.create(
            num=2,
            on_street='Kirova',
            project=self.project,
            image='image2.jpg',
        )

    def test_get_all_buildings(self):
        buildings = BuildingRepository.get_all_buildings()
        self.assertEqual(len(buildings), 2)

        building_data = buildings[0]
        self.assertEqual(building_data.id, self.building1.id)
        self.assertEqual(building_data.num, self.building1.num)
        self.assertEqual(building_data.on_street, self.building1.on_street)
        self.assertEqual(building_data.project_id, self.project.id)
        self.assertEqual(building_data.image_url, self.building1.image)

    def test_get_building_by_id_success(self):
        building_data = BuildingRepository.get_building_by_id(self.building1.id)

        self.assertEqual(building_data.id, self.building1.id)
        self.assertEqual(building_data.num, self.building1.num)
        self.assertEqual(building_data.on_street, self.building1.on_street)
        self.assertEqual(building_data.project_id, self.project.id)
        self.assertEqual(building_data.image_url, self.building1.image)

    def test_get_building_by_id_fail(self):
        with self.assertRaises(ValueError) as context:
            BuildingRepository.get_building_by_id(10)
        self.assertEqual(str(context.exception), 'Ошибка! Корпус с id 10 не существует')