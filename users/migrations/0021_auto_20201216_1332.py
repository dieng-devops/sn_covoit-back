# Generated by Django 3.0.7 on 2020-12-16 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20201216_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='proprietaire',
            new_name='added_by',
        ),
    ]
