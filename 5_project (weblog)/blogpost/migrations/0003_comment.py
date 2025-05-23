# Generated by Django 5.0.4 on 2025-05-07 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0002_alter_blogpost_likes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.TextField(blank=True)),
                ("city", models.CharField(blank=True, max_length=255)),
                ("province", models.CharField(blank=True, max_length=255)),
                ("zip_code", models.CharField(blank=True, max_length=11)),
                ("hide_name", models.BooleanField(default=True)),
                ("comment", models.TextField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blogpost.blogpost",
                    ),
                ),
            ],
        ),
    ]
