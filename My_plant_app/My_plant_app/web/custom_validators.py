from django.core.exceptions import ValidationError
import re


def capital_letter(name):
    if name[0].islower():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters(plant):
    pattern = r'^[A-Za-z]+$'
    if not re.match(pattern, plant):
        raise ValidationError('Plant name should contain only letters!')