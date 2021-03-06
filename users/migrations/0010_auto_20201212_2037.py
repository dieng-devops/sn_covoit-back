# Generated by Django 3.0.7 on 2020-12-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201212_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='discussion',
            field=models.BooleanField(choices=[(True, "J'aime discuter parfois"), (False, "Je n'aime pas discuter quand je conduis")], default=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='fumeur',
            field=models.BooleanField(choices=[(True, "J'accepte la fumée"), (False, "Je n'aime pas la fumée dans la voiture")], default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='musique',
            field=models.BooleanField(choices=[(True, "J'aime bien écouter de la musique"), (False, "Je n'aime pas écouter de la musique en conduisant")], default=True),
        ),
    ]
