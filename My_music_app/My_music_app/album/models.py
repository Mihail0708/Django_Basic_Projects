from django.core.validators import MinValueValidator

from django.db import models


class Album(models.Model):
    CHOICES = [
        ('Pop Music', "Pop Music"),
        ('Jazz Music', "Jazz Music"),
        ('R&B Music', "R&B Music"),
        ('Rock Music', "Rock Music"),
        ('Country Music', "Country Music"),
        ('Dance Music', "Dance Music"),
        ('Hip Hop Music', "Hip Hop Music"),
        ('Other', "Other")
    ]

    album_name = models.CharField(unique=True, max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=CHOICES)
    description = models.TextField(blank=True, null=True)
    image_URL = models.URLField()
    price = models.FloatField(validators=(MinValueValidator(0.0),))

