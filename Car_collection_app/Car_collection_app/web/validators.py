from django.core.exceptions import ValidationError


def min_length(name):
    if len(name) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def year_check(year):
    if 1980 > year or year > 2049:
        raise ValidationError('Year must be between 1980 and 2049')