# Generated by Django 3.0.3 on 2020-05-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200503_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
    ]
