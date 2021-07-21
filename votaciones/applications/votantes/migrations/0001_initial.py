# Generated by Django 3.2.5 on 2021-07-12 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Votantes',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')], verbose_name='Numero de identificación')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('dependencia', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('estado_voto', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Votante',
                'verbose_name_plural': 'Votantes',
            },
        ),
    ]
