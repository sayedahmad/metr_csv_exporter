# Generated by Django 4.2.2 on 2023-07-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]