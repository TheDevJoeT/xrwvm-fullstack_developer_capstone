from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime



class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # optional extra fields (allowed by instructions)
    country = models.CharField(max_length=50, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



class CarModel(models.Model):

    # Many models belong to one make
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="models"
    )

    # dealer id from Cloudant
    dealer_id = models.IntegerField()

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    ]

    type = models.CharField(
        max_length=15,
        choices=CAR_TYPES,
        default='SEDAN'
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(datetime.now().year)
        ]
    )

    # optional extra field
    msrp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
