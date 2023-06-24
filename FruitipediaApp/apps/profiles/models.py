from django.db import models
from django.core import validators
from FruitipediaApp.apps.validators import validate_is_first_char_letter

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        verbose_name='First Name',
        validators=[
            validators.MinLengthValidator(2),
            validate_is_first_char_letter
        ]
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        verbose_name='Last Name',
        validators=[
            validators.MinLengthValidator(2),
            validate_is_first_char_letter
        ]
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(8),
        ]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )



