# Generated by Django 3.0.7 on 2020-12-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0075_auto_20201220_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='role',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='role',
            field=models.ManyToManyField(related_name='roles', to='users.Role'),
        ),
    ]
