from django.db import models

class Apartment(models.Model):
    on_floor = models.IntegerField(verbose_name='Количество квартир на этаже')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    total_area = models.IntegerField(verbose_name='Общая площадь')
    living_area = models.IntegerField(verbose_name='Жилая площадь')
    kitchen_area = models.IntegerField(verbose_name='Площадь кухни')
    is_balcony = models.BooleanField(verbose_name='Наличие балкона')
    price_square = models.IntegerField(verbose_name='Цена за кв.м.')
    price_flat = models.IntegerField(verbose_name='Цена за квартиру')
    on_sale = models.BooleanField(default=True, verbose_name='В продаже')
