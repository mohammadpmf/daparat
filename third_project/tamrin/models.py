from django.db import models
from django.contrib.auth import get_user_model


class Car(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='test salam')
    price_toman = models.IntegerField(null=True, blank=True)
    price_takhfif = models.DecimalField(max_digits=4, decimal_places=1)  #  xxx.x
    # test5 = models.FloatField()
    is_ready = models.BooleanField(default=True)
    date_created = models.DateField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True, blank=True)
    site_address = models.URLField(null=True, blank=True)
    test12 = models.SlugField(null=True, blank=True)
    test13 = models.ImageField(null=True, blank=True)
    test14 = models.FileField(null=True, blank=True)
    test15 = models.GenericIPAddressField(null=True, blank=True)
    test16 = models.UUIDField(null=True, blank=True)
    test17 = models.JSONField(null=True, blank=True)
    test18 = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    # test19 = models.OneToOneField()
    # test20 = models.ManyToManyField()