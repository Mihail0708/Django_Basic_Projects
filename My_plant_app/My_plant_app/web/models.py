from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from My_plant_app.web.custom_validators import capital_letter, only_letters


class Profile(models.Model):
    username = models.CharField(validators=(MaxLengthValidator(10), MinLengthValidator(2),))
    first_name = models.CharField(max_length=20, validators=(capital_letter,))
    last_name = models.CharField(max_length=20, validators=(capital_letter,))
    profile_picture= models.URLField(blank=True, null=True)


class Plant(models.Model):
    CHOICES = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    ]
    plant_type = models.CharField(max_length=14, choices=CHOICES)
    name = models.CharField(validators=(MaxLengthValidator(20), MinLengthValidator(2), only_letters,))
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

