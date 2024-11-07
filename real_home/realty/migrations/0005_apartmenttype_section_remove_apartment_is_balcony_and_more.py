# Generated by Django 5.1.2 on 2024-11-07 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_remove_floor_floor_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane', models.CharField(max_length=100, null=True, verbose_name='Планировка')),
                ('rooms', models.IntegerField(verbose_name='Количество комнат')),
                ('total_area', models.IntegerField(verbose_name='Общая площадь')),
                ('living_area', models.IntegerField(verbose_name='Жилая площадь')),
                ('kitchen_area', models.IntegerField(verbose_name='Площадь кухни')),
                ('is_balcony', models.BooleanField(verbose_name='Наличие балкона')),
                ('price_square', models.IntegerField(verbose_name='Цена за кв.м.')),
                ('price_flat', models.IntegerField(verbose_name='Цена за квартиру')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Секция')),
            ],
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='is_balcony',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='kitchen_area',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='living_area',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='on_floor',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='price_flat',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='price_square',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='rooms',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='total_area',
        ),
        migrations.AddField(
            model_name='apartment',
            name='num',
            field=models.IntegerField(null=True, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='realty.floor', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='on_sale',
            field=models.BooleanField(null=True, verbose_name='В продаже'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='realty.apartmenttype', verbose_name='Тип квартиры'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='realty.section', verbose_name='Секция'),
        ),
        migrations.AddField(
            model_name='floor',
            name='section',
            field=models.ManyToManyField(related_name='floors', to='realty.section', verbose_name='Секция'),
        ),
    ]