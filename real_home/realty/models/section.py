from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=10, verbose_name='Секция', null=True)
    building = models.ForeignKey('Building',
                                 on_delete=models.CASCADE,
                                 related_name='sections',
                                 verbose_name='Корпус',
                                 null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'building'], name='unique_section_per_building')
        ]

    def __str__(self):
        return f'Секция {self.name} в корпусе №{self.building}'