from django.db import models


class Floor(models.Model):
    section = models.ManyToManyField('Section', related_name='floors', verbose_name='Секция')

    def __str__(self):
        return f'Этаж {self.id}'