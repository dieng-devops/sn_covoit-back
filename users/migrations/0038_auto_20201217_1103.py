# Generated by Django 3.0.7 on 2020-12-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20201217_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localite',
            name='type_locatite',
            field=models.CharField(choices=[('Region', 'Region'), ('Departement', 'Departement'), ('Commune', 'Commune'), ('Village', 'Village')], default='Commune', max_length=15, verbose_name='Type de la localité'),
        ),
    ]
