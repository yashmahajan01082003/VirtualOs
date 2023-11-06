# Generated by Django 4.2.3 on 2023-07-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_bottomsideicons"),
    ]

    operations = [
        migrations.CreateModel(
            name="HandGest",
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
                ("img", models.ImageField(upload_to="hand_gestures_images")),
                ("func", models.CharField(default=" ", max_length=255)),
            ],
            options={
                "verbose_name_plural": "HandGest",
            },
        ),
    ]
