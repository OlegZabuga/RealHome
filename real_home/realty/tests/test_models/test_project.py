from django.test import TestCase
from realty.models import Project
from unittest.mock import MagicMock


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project_without_image = Project.objects.create(
            name='first',
            description='first',
            amount_floors=10,
            rating='A',
            image=None
        )

        self.project_with_image = Project.objects.create(
            name='second',
            description='second',
            amount_floors=10,
            rating='A',
        )

        self.project_with_image.image = MagicMock()
        self.project_with_image.image.url = '/media/images/test_image.jpg'


    def test_str_representation(self):
        '''Тест для строкового представления проекта'''
        self.assertEqual(
            str(self.project_without_image),
            f'Проект {self.project_without_image.name}, {self.project_without_image.amount_floors} этажный дом, класса {self.project_without_image.rating}'
        )


    def test_image_tag_with_image(self):
        '''Тест функции image_tag для проекта с изображением'''
        expected_html = '<img src="/media/images/test_image.jpg" width="100" />'
        self.assertEqual(self.project_with_image.image_tag(), expected_html)


    def test_image_tag_without_image(self):
        '''Тест функции image_tag для проекта без изображения'''
        self.assertEqual(self.project_without_image.image_tag(), 'No image')