# Generated by Django 2.2.24 on 2022-10-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20221023_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='owner_flats',
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
