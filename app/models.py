from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):                                              # Модель: база данных репертуара "Песня"
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)


class Band(models.Model):                                               # Модель: база данных кавер-групп Cover Bands
    band_name = models.CharField(max_length=100)


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


class Audio(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField()


class ExportFolderName(models.Model):
    subject = models.CharField(max_length=125)
    name = models.CharField(max_length=125)
