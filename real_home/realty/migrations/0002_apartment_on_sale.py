# Generated by Django 5.1.2 on 2024-11-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='on_sale',
            field=models.BooleanField(default=True, verbose_name='В продаже'),
        ),
    ]