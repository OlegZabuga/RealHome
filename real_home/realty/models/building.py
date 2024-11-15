from django.db import models
from django.utils.safestring import mark_safe


class Building(models.Model):
    num = models.IntegerField(verbose_name='Номер дома', null=True)
    on_street = models.CharField(max_length=150, verbose_name='Адрес дома', null=True)
    project = models.ForeignKey('Project',
                                on_delete=models.CASCADE,
                                related_name='buildings',
                                null=True,
                                verbose_name='Проект дома')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение корпуса')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'

    def __str__(self):
        return f'Корпус {self.num} на улице {self.on_street}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{ self.image.url }" width="100" />')
        return 'No image'

    image_tag.short_description = 'Изображение корпуса'