# Generated by Django 4.2.4 on 2023-09-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0009_alter_route_distance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="distance",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]