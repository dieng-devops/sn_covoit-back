# Generated by Django 3.0.7 on 2020-12-19 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0067_auto_20201219_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajet',
            name='members',
            field=models.ManyToManyField(limit_choices_to={'profile_actif': True}, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]