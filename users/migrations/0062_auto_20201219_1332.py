# Generated by Django 3.0.7 on 2020-12-19 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20201219_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='nextofkin',
            name='member',
        ),
        migrations.RemoveField(
            model_name='passagerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='specialities',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trajet',
            name='members',
        ),
        migrations.DeleteModel(
            name='ConducteurProfile',
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
        migrations.DeleteModel(
            name='NextOfKin',
        ),
        migrations.DeleteModel(
            name='PassagerProfile',
        ),
        migrations.DeleteModel(
            name='TrainerProfile',
        ),
        migrations.DeleteModel(
            name='TrainerSpeciality',
        ),
    ]
