from django.db import models


class Car(models.Model):
    GEAR_TYPE_CHOICES = (
        ("automat", "اتوماتیک"),
        ("manual", "دستی")
    )
    brand = models.CharField(max_length=63)
    color = models.CharField(max_length=63)
    model = models.CharField(max_length=63)
    date = models.DateField()
    price = models.PositiveIntegerField()
    country = models.CharField(max_length=63)
    accelerate = models.DecimalField(max_digits=4, decimal_places=3)
    gear_type = models.CharField(max_length=63, choices=GEAR_TYPE_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
