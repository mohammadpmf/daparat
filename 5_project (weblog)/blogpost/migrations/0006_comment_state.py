# Generated by Django 5.0.4 on 2025-06-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0005_alter_comment_address_alter_comment_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="state",
            field=models.CharField(
                default="p", max_length=1, verbose_name="وضعیت کامنت"
            ),
        ),
    ]
