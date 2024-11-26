from django.test import TestCase
from realty.domain import Apartment, Building, Section, Floor, ApartmentType
from django.db import IntegrityError
from unittest.mock import MagicMock


class ApartmentModelTest(TestCase):
    def setUp(self):
        self.type = ApartmentType.objects.create(plane='Студия')
        self.building = Building.objects.create(num=8)
        self.section = Section.objects.create(name='1', building=self.building)
        self.floor = Floor.objects.create(floor_number=1, section=self.section)

        self.apartment_without_image = Apartment.objects.create(
            num=5,
            on_sale=True,
            type=self.type,
            floor=self.floor,
            section=self.section,
            building=self.building,
            image=None
        )

        self.apartment_with_image = Apartment.objects.create(
            num=6,
            on_sale=True,
            type=self.type,
            floor=self.floor,
            section=self.section,
            building=self.building,
        )

        self.apartment_with_image.image = MagicMock()
        self.apartment_with_image.image.url = '/media/images/test_image.jpg'

    def test_str_representation(self):
        '''Тест для строкового представления квартиры'''
        self.assertEqual(
            str(self.apartment_without_image),
            f'Квартира №{self.apartment_without_image.num} в корпусе №{self.apartment_without_image.building}'
        )

    def test_unique_apartment_per_building(self):
        '''Тест для проверки уникальности номера квартиры для каждого корпуса'''
        with self.assertRaises(IntegrityError):
            Apartment.objects.create(
                num=5,
                on_sale=True,
                type=self.type,
                floor=self.floor,
                section=self.section,
                building=self.building,
                image=None
            )

    def test_image_tag_with_image(self):
        '''Тест функции image_tag для квартиры с изображением'''
        excpected_html = '<img src="/media/images/test_image.jpg" width="100" />'
        self.assertEqual(self.apartment_with_image.image_tag(), excpected_html)

    def test_image_tag_without_image(self):
        '''Тест функции image_tag для квартиры без изображения'''
        self.assertEqual(self.apartment_without_image.image_tag(), 'No image')