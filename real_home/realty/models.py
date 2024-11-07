from django.db import models


class Apartment(models.Model):
    num = models.IntegerField(null=True, verbose_name='Номер квартиры')
    on_sale = models.BooleanField(verbose_name='В продаже', null=True)
    type = models.ForeignKey('ApartmentType', null=True, on_delete=models.PROTECT, verbose_name='Тип квартиры')
    floor = models.ForeignKey('Floor', on_delete=models.PROTECT, null=True, verbose_name='Этаж')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name='Секция')

    def __str__(self):
        return f'Квартира №{self.num} на этаже {self.floor}'


class ApartmentType(models.Model):
    plane = models.CharField(max_length=100, verbose_name='Планировка', null=True)
    rooms = models.IntegerField(verbose_name='Количество комнат')
    total_area = models.IntegerField(verbose_name='Общая площадь')
    living_area = models.IntegerField(verbose_name='Жилая площадь')
    kitchen_area = models.IntegerField(verbose_name='Площадь кухни')
    is_balcony = models.BooleanField(verbose_name='Наличие балкона')
    price_square = models.IntegerField(verbose_name='Цена за кв.м.')
    price_flat = models.IntegerField(verbose_name='Цена за квартиру')

    def __str__(self):
        return self.plane


class Floor(models.Model):
    amount_flats = models.IntegerField(null=True, blank=True, verbose_name='Количество квартир на этаже')
    section = models.ManyToManyField('Section', related_name='floors', verbose_name='Секция')

    def __str__(self):
        return f'Этаж {self.id}'


class Section(models.Model):
    name = models.CharField(max_length=10, verbose_name='Секция')

    def __str__(self):
        return f'Секция {self.name}'
