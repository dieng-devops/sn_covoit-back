# Generated by Django 3.0.7 on 2020-12-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201212_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_actif',
            field=models.BooleanField(default=False),
        ),
    ]