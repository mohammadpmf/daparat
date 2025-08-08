from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.shortcuts import reverse


class FoodType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"


class Food(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="foods/")
    food_types = models.ManyToManyField(to=FoodType)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    


class SuggestionCritics(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField()


class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11, "کمتر از ۱۱ رقم وارد نکنید."), MaxLengthValidator(11, "بیشتر از ۱۱ رقم وارد نکنید.")])
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1, "سفارش باید بیش از ۱ عدد باشد."), MaxValueValidator(10, "سفارش باید کمتر از ۱۱ عدد باشد.")])
