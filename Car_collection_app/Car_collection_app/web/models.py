from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from Car_collection_app.web.validators import min_length, year_check


class Profile(models.Model):
    username = models.CharField(validators=(MaxLengthValidator(10), min_length,))
    email = models.EmailField()
    age = models.IntegerField(validators=(MinValueValidator(18),))
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)


class Car(models.Model):
    CARS = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ]
    type = models.CharField(max_length=10, choices=CARS)
    model = models.CharField(validators=(MinLengthValidator(2), MaxLengthValidator(20),))
    year = models.IntegerField(validators=(year_check,))
    image_Url = models.URLField()
    price = models.FloatField(validators=(MinValueValidator(1),))

