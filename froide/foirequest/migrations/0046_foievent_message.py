# Generated by Django 3.0.8 on 2020-07-29 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foirequest", "0045_auto_20200728_1537"),
    ]

    operations = [
        migrations.AddField(
            model_name="foievent",
            name="message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="foirequest.FoiMessage",
            ),
        ),
    ]
