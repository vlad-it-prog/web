# Generated by Django 3.1.1 on 2021-01-10 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_band_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='track',
        ),
    ]
