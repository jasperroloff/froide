# Generated by Django 2.2.4 on 2019-10-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publicbody", "0026_publicbody_wikidata_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publicbody",
            name="wikidata_item",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="wikidata item"
            ),
        ),
    ]
