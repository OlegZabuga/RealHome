from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name='Проект жилого дома', unique=True)
    description = models.TextField(verbose_name='Описание домов проекта')
    amount_floors = models.IntegerField(verbose_name='Количество этажей')
    rating = models.CharField(max_length=1, verbose_name='Класс дома')

    def __str__(self):
        return f'Проект {self.name}, {self.amount_floors} этажный дом, класса {self.rating}'