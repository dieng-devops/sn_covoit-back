# Generated by Django 3.0.7 on 2020-12-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20201216_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='added_by',
            field=models.CharField(default='email', max_length=150),
        ),
    ]
