from django.db import models


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