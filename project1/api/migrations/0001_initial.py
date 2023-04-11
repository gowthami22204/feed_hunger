# Generated by Django 4.1.7 on 2023-04-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VolunteerUser",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("volunteername", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("passcode", models.CharField(max_length=200)),
                (
                    "Areaofinterest",
                    models.CharField(
                        choices=[
                            ("1", "medical"),
                            ("2", "food"),
                            ("3", "scribe"),
                            ("4", "others"),
                        ],
                        default="1",
                        max_length=50,
                    ),
                ),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
            ],
        ),
    ]