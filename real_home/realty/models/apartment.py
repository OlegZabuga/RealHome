from django.db import models


class Apartment(models.Model):
    num = models.IntegerField(null=True, verbose_name='Номер квартиры')
    on_sale = models.BooleanField(verbose_name='В продаже', null=True)
    type = models.ForeignKey('ApartmentType', null=True, on_delete=models.PROTECT, verbose_name='Тип квартиры')
    floor = models.ForeignKey('Floor', on_delete=models.PROTECT, null=True, verbose_name='Этаж')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name='Секция')

    def __str__(self):
        return f'Квартира №{self.num} на этаже {self.floor}'