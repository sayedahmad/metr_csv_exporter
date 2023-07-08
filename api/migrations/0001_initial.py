# Generated by Django 4.2.2 on 2023-07-06 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("device_id", models.BigIntegerField(blank=True, null=True)),
                ("device_type", models.IntegerField()),
                ("status", models.IntegerField()),
                ("version", models.IntegerField()),
                ("access_number", models.IntegerField()),
                ("manufacturer", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
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
                ("dimension", models.CharField(max_length=100)),
                ("newest_value", models.IntegerField()),
                ("due_date_value", models.IntegerField(blank=True, null=True)),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.IntegerField(choices=[(1, "Measurement"), (2, "Error")]),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_measurements",
                        to="api.device",
                    ),
                ),
            ],
        ),
    ]