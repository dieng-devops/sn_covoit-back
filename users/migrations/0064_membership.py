# Generated by Django 3.0.7 on 2020-12-19 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0063_useraccount_profile_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('personne', models.OneToOneField(limit_choices_to={'role': 'Passager'}, on_delete=django.db.models.deletion.CASCADE, related_name='members_profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membership',
            },
        ),
    ]
