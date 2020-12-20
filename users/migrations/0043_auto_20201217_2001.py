# Generated by Django 3.0.7 on 2020-12-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_trajet_conducteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajet',
            name='conducteur',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='users.UserAccount'),
        ),
        migrations.AlterField(
            model_name='trajet',
            name='etapes',
            field=models.ManyToManyField(related_name='etapes', to='users.Localite'),
        ),
    ]