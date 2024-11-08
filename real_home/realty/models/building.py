from django.db import models


class Building(models.Model):
    num = models.IntegerField(verbose_name='Номер дома', null=True)
    on_street = models.CharField(max_length=150, verbose_name='Адрес дома', null=True)

    def __str__(self):
        return f'Корпус {self.num} на улице {self.on_street}'