# Generated by Django 3.1.1 on 2020-11-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
    ]