# Generated by Django 5.0.4 on 2025-04-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tamrin", "0002_alter_car_description_alter_car_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=models.TextField(blank=True, default="test salam"),
        ),
        migrations.AlterField(
            model_name="car",
            name="price_toman",
            field=models.IntegerField(blank=True),
        ),
    ]
