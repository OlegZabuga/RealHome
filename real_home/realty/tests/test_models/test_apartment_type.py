from django.test import TestCase
from realty.models import ApartmentType


class ApartmentTypeModelTest(TestCase):
    def setUp(self):
        self.type = ApartmentType.objects.create(
            plane='Студия',
        )


    def test_str_representation(self):
        '''Тест для строкового отображения типа квартиры'''
        self.assertEqual(
            str(self.type),
            self.type.plane
        )