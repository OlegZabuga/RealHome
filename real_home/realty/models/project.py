from django.db import models
from django.utils.safestring import mark_safe


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name='Проект жилого дома', unique=True)
    description = models.TextField(verbose_name='Описание домов проекта')
    amount_floors = models.IntegerField(verbose_name='Количество этажей')
    rating = models.CharField(max_length=1, verbose_name='Класс дома')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Эмблема проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект {self.name}, {self.amount_floors} этажный дом, класса {self.rating}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{ self.image.url }" width="100" />')
        return 'No image'

    image_tag.short_description = 'Изображение проекта'