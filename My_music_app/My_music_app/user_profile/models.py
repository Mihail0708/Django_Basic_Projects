from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from My_music_app.user_profile.validators import validator_user_name


class Profile(models.Model):
    username = models.CharField(validators=(MinLengthValidator(2), MaxLengthValidator(15), validator_user_name))
    email = models.EmailField(null=False, blank=False)
    age = models.PositiveIntegerField(blank=True, null=True)

