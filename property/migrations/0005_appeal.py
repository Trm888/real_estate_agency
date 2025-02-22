# Generated by Django 2.2.24 on 2022-10-21 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20221021_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='appeals_flat', to='property.Flat',
                                           verbose_name='Объект жалобы')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='appeals_user',
                                           to=settings.AUTH_USER_MODEL,
                                           verbose_name='Жалоба от')),
            ],
        ),
    ]
