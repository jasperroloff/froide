# Generated by Django 2.1.9 on 2019-08-16 14:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0021_auto_20190309_1226"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountBlacklist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("address", models.TextField(blank=True)),
                ("email", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "Blacklist entry",
                "verbose_name_plural": "Blacklist",
            },
        ),
    ]
