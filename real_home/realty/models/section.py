from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=10, verbose_name='Секция')

    def __str__(self):
        return f'Секция {self.name}'