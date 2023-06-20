# Generated by Django 4.2.2 on 2023-06-19 07:16

import My_plant_app.web.custom_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "plant_type",
                    models.CharField(
                        choices=[
                            ("Outdoor Plants", "Outdoor Plants"),
                            ("Indoor Plants", "Indoor Plants"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        validators=[
                            django.core.validators.MaxLengthValidator(20),
                            django.core.validators.MinLengthValidator(2),
                            My_plant_app.web.custom_validators.only_letters,
                        ]
                    ),
                ),
                ("image_url", models.URLField()),
                ("description", models.TextField()),
                ("price", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        validators=[
                            django.core.validators.MaxLengthValidator(10),
                            django.core.validators.MinLengthValidator(2),
                        ]
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=20,
                        validators=[My_plant_app.web.custom_validators.capital_letter],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=20,
                        validators=[My_plant_app.web.custom_validators.capital_letter],
                    ),
                ),
                ("profile_picture", models.URLField(blank=True, null=True)),
            ],
        ),
    ]