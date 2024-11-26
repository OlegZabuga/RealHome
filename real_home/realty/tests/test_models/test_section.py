from django.test import TestCase
from realty.domain import Section, Building
from django.db import IntegrityError


class SectionModelTest(TestCase):
    def setUp(self):
        self.building = Building.objects.create(num=8)

        self.section = Section.objects.create(
            name = '1',
            building = self.building
        )


    def test_str_representation(self):
        '''Тест для строкового представления секции'''
        self.assertEqual(
            str(self.section),
            f'Секция {self.section.name} в корпусе №{self.building}'
        )


    def test_unique_section_per_building(self):
        '''Тест проверки уникальности секции для одного корпуса'''
        with self.assertRaises(IntegrityError):
            Section.objects.create(
                name = '1',
                building = self.building
            )