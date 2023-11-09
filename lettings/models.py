from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
        number (PositiveIntegerField): The number of the address.
        street (CharField): The street of the address.
        city (CharField): The city of the address.
        state (CharField): The state of the address.
        zip_code (PositiveIntegerField): The zip code of the address.
        country_iso_code (CharField): The ISO code of the country.

    Methods:
        __str__: Returns a string representation of the address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
