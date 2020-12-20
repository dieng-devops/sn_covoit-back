# Generated by Django 3.0.7 on 2020-12-16 17:00

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20201216_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
        ),
        migrations.AddField(
            model_name='region',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
        ),
    ]
