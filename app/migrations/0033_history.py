# Generated by Django 3.1.1 on 2021-01-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateTimeField()),
                ('month', models.DateTimeField()),
                ('day', models.DateTimeField()),
                ('hour', models.DateTimeField()),
                ('minute', models.DateTimeField()),
                ('second', models.DateTimeField()),
            ],
        ),
    ]
