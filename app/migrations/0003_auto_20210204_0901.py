# Generated by Django 3.1.1 on 2021-02-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210204_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('song_name', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=100)),
                ('another_track_mark', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='tracks',
            field=models.ManyToManyField(to='app.Track'),
        ),
    ]
