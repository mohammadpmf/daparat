from django.db import models

from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    surname = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    age = models.PositiveIntegerField(verbose_name=_("Age"))
    age2 = models.PositiveIntegerField(verbose_name=_("Age2"), blank=True, null=True)
