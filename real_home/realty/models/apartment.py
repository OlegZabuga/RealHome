from django.db import models
from django.utils.safestring import mark_safe


class Apartment(models.Model):
    num = models.IntegerField(null=True, verbose_name='Номер квартиры')
    on_sale = models.BooleanField(verbose_name='В продаже', default=True)
    type = models.ForeignKey('ApartmentType', null=True, on_delete=models.PROTECT, verbose_name='Тип квартиры')
    floor = models.ForeignKey('Floor', on_delete=models.PROTECT, null=True, verbose_name='Этаж')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name='Секция')
    building = models.ForeignKey('Building', null=True, on_delete=models.CASCADE, verbose_name='Корпус')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение квартиры')

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'
        constraints = [
            models.UniqueConstraint(fields=['num', 'building'], name='unique_apartment_per_building')
        ]

    def __str__(self):
        return f'Квартира №{self.num} в корпусе №{self.building}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{ self.image.url }" width="100" />')
        return 'No image'

    image_tag.short_description = 'Изображение для квартиры'