import re

from django.core.exceptions import ValidationError


def validator_user_name(username):
    pattern = r'^[A-Za-z_0-9]+$'
    if not re.match(pattern, username):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')