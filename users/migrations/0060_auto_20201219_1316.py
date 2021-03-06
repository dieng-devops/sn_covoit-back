# Generated by Django 3.0.7 on 2020-12-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20201218_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='trajet',
            name='members',
            field=models.ManyToManyField(to='users.PassagerProfile'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('Trainer', 'Trainer'), ('Member', 'Member'), ('Passager', 'Passager'), ('Conducteur', 'Conducteur')], default='Passager', max_length=15),
        ),
    ]
