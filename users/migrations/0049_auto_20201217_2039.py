# Generated by Django 3.0.7 on 2020-12-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_auto_20201217_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajet',
            name='prix_ttc',
            field=models.PositiveIntegerField(verbose_name='Prix unitaire HT'),
        ),
    ]
