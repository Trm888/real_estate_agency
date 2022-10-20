# Generated by Django 2.2.24 on 2022-10-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True, verbose_name='New building'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='construction_year',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год постройки здания'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='living_area',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='количество жилых кв.метров'),
        ),
    ]
