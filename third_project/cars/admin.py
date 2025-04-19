from django.contrib import admin

from . import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "brand", "color", "accelerate", "datetime_modified", "price"]
    list_display_links = ["id", "brand", "accelerate", "datetime_modified"]
    list_editable = ["price", "color"]


# admin.site.register(models.Car, CarAdmin)