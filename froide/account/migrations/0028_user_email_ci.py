# Generated by Django 3.1.8 on 2021-04-28 10:24

import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0027_auto_20210412_1518"),
    ]

    operations = [
        CITextExtension(),
        migrations.AddField(
            model_name="user",
            name="email_ci",
            field=django.contrib.postgres.fields.citext.CIEmailField(
                blank=True, max_length=254, null=True, verbose_name="email address"
            ),
        ),
    ]
