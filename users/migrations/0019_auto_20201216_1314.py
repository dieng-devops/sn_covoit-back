# Generated by Django 3.0.7 on 2020-12-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20201216_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='proprietaire',
            field=models.CharField(default='settings.AUTH_USER_MODEL', max_length=150),
        ),
    ]
