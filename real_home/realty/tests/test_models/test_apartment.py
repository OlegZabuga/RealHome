from math import floor

from PIL.ImImagePlugin import number
from django.test import TestCase
from realty.models import Apartment, Building, Section, Floor, ApartmentType


class ApartmentModelTest(TestCase):
    def setUp(self):
        self.type = ApartmentType.objects.create(plane='Студия')
        self.building = Building.objects.create(num='8')
        self.section = Section.objects.create(name='1', building=self.building)
        self.floor = Floor.objects.create(floor_number=1, section=self.section)

        self.apartment = Apartment.objects.create(
            num=5,
            on_sale=True,
            type=self.type,
            floor=self.floor,
            section=self.section,
            building=self.building,
            image=None
        )

    def test_str_representation(self):
        '''Тест для строкового представления'''
        self.assertEqual(
            str(self.apartment),
            f'Квартира №{self.apartment.num} в корпусе №{self.apartment.building}'
        )