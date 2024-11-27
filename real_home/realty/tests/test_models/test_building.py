from django.test import TestCase
from realty.models import Building, Project
from unittest.mock import MagicMock


class BuildingModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name='first_project',
                                              description='first_description',
                                              amount_floors='10',
                                              rating='A')

        self.building_without_image = Building.objects.create(
            num=8,
            on_street='Test_street',
            project=self.project,
            image=None
        )

        self.building_with_image = Building.objects.create(
            num=10,
            on_street='Test_street',
            project=self.project
        )

        self.building_with_image.image = MagicMock()
        self.building_with_image.image.url  = '/media/images/test_image.jpg'

    def test_str_representation(self):
        '''Тест для проверки строкового отображения'''
        self.assertEqual(
            str(self.building_without_image),
            f'Корпус {self.building_without_image.num} на улице {self.building_without_image.on_street}'
        )


    def test_image_tag_with_image(self):
        '''Тест функции image_tag с изображением корпуса'''
        expected_html = '<img src="/media/images/test_image.jpg" width="100" />'
        self.assertEqual(self.building_with_image.image_tag(), expected_html)


    def test_image_tag_without_image(self):
        '''Тест функции image_tag без изображения корпуса'''
        self.assertEqual(self.building_without_image.image_tag(), 'No image')