from django.db import models
from django.contrib.auth.models import User


class Songs(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)


class Band(models.Model):
    band = models.CharField(max_length=100)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)


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