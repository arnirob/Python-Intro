# Generated by Django 3.0.3 on 2020-05-03 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_listing_bathrooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
    ]
