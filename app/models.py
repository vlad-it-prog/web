from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Track(models.Model):                                              # Модель: база данных репертуара "Песня"
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=100)
    another_track_mark = models.BooleanField()

    def __str__(self):
        return self.artist_name + " - " + self.song_name + " - " + self.language_code

    # def __str__(self):
    #     return self.artist_name
    #
    # def __str__(self):
    #     return self.song_name


class Band(models.Model):                                               # Модель: база данных кавер-групп Cover Bands
    band_name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.band_name


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


class Images(models.Model):                                                # Модель: база данных "Изображения"
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Song(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField()


class ExportFolderName(models.Model):
    subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)


class ImportFolderName(models.Model):
    subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)


class ExportFileName(models.Model):
    # subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)


class OtherTrackList(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)


class History(models.Model):
    time = models.DateTimeField()
    event = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    def __str__(self):
        return format(self.time.strftime('%d.%m.%Y %H:%M'))
        # return 'Заявка от {}'.format(self.time.strftime('%d.%m.%Y %H:%M'))
    #
    # def __str__(self):
    #     return self.event
    #
    # def __str__(self):
    #     return self.user


