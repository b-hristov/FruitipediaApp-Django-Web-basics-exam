from django.db import models
from django.core import validators
from FruitipediaApp.apps.validators import validate_is_all_letters

# Create your models here.


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
            validate_is_all_letters
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)

