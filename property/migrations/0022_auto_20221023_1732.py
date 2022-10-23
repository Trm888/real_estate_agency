# Generated by Django 2.2.24 on 2022-10-23 11:32

from django.db import migrations

def get_owner_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all():
        owners_all_flats = Flat.objects.filter(owner=owner.owner)
        for flat in owners_all_flats:
            owner.owner_flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_owner_owner_flats'),
    ]

    operations = [migrations.RunPython(get_owner_flats),
    ]
