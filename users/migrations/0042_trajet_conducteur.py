# Generated by Django 3.0.7 on 2020-12-17 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_trajet_date_arrivee'),
    ]

    operations = [
        migrations.AddField(
            model_name='trajet',
            name='conducteur',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
