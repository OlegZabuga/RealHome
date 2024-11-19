from django.db import models


class Floor(models.Model):
    floor_number = models.IntegerField(verbose_name='Номер этажа', null=True)
    section = models.ForeignKey('Section',
                                on_delete=models.CASCADE,
                                related_name='floors',
                                verbose_name='Секция',
                                null=True)

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'
        constraints = [
            models.UniqueConstraint(fields=['floor_number', 'section'], name='unique_floor_per_section')
        ]

    def __str__(self):
        return f'Этаж {self.floor_number} в секции {self.section}'