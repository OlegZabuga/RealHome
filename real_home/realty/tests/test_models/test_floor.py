from django.db import IntegrityError
from django.test import TestCase
from realty.domain import Floor, Section


class FloorModelTest(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='1')

        self.floor_first = Floor.objects.create(
            floor_number=1,
            section=self.section,
        )

    def test_str_representation(self):
        '''Тест для строкового представления этажа'''
        self.assertEqual(
            str(self.floor_first),
            f'Этаж {self.floor_first.floor_number} в секции {self.section}'
        )

    def test_unique_floor_per_section(self):
        '''Тест проверки уникальности каждого этажа для одной секции'''
        with self.assertRaises(IntegrityError):
            Floor.objects.create(
                floor_number=1,
                section=self.section
            )