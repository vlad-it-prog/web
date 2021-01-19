from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Track(models.Model):                                              # Модель: база данных репертуара "Песня"
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name + self.song_name


class Band(models.Model):                                               # Модель: база данных кавер-групп Cover Bands
    band_name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)


class Client(models.Model):
    address = models.CharField('Address', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(
        max_length=100
    )
    credit_card_number = models.CharField(
        max_length=90
    )


class Cash(models.Model):                                               # Модель: база данных "тестовая"
    name = models.CharField(max_length=100)                             # - для кеширования данных


class Cat(models.Model):                                                # Модель: база данных "Изображения"
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Song(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField()


class ExportFolderName(models.Model):
    subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)


class ExportFileName(models.Model):
    # subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)


class OtherTrackList(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)


class HistoryTime(models.Model):
    created = models.DateTimeField()

    def __str__(self):
        return 'Заявка от {}'.format(self.created.strftime('%d.%m.%Y %H:%M'))


