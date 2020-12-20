# Generated by Django 3.0.7 on 2020-12-18 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0054_auto_20201218_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='fait_sur',
        ),
        migrations.AddField(
            model_name='avis',
            name='auteur',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Avis fait par'),
        ),
        migrations.AddField(
            model_name='avis',
            name='avis_sur',
            field=models.CharField(default='', max_length=70, verbose_name='Avis donné sur'),
        ),
        migrations.AddField(
            model_name='avis',
            name='trajet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='users.Trajet'),
        ),
    ]
