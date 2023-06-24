from django.core import exceptions


def validate_is_first_char_letter(value):
    if not value[0].isalpha():
        raise exceptions.ValidationError('Your name must start with a letter!')


def validate_is_all_letters(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Fruit name should contain only letters!')
