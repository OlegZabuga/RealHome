# Generated by Django 5.1.2 on 2024-11-08 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Проект жилого дома')),
                ('description', models.TextField(verbose_name='Описание домов проекта')),
                ('amount_floors', models.IntegerField(verbose_name='Количество этажей')),
                ('rating', models.CharField(max_length=1, verbose_name='Класс дома')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='realty.project', verbose_name='Проект дома'),
        ),
    ]
