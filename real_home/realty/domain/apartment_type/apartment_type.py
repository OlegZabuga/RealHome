from django.db import models


class ApartmentType(models.Model):
    plane = models.CharField(max_length=100, verbose_name='Планировка', null=True)
    rooms = models.IntegerField(verbose_name='Количество комнат', null=True)
    total_area = models.IntegerField(verbose_name='Общая площадь', null=True)
    living_area = models.IntegerField(verbose_name='Жилая площадь', null=True)
    kitchen_area = models.IntegerField(verbose_name='Площадь кухни', null=True)
    is_balcony = models.BooleanField(verbose_name='Наличие балкона', null=True)
    price_square = models.IntegerField(verbose_name='Цена за кв.м.', null=True)
    price_flat = models.IntegerField(verbose_name='Цена за квартиру', null=True)

    class Meta:
        verbose_name = 'Тип квартиры'
        verbose_name_plural = 'Типы квартир'

    def __str__(self):
        return self.plane