# Generated by Django 3.2.5 on 2021-07-09 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votantes', '0002_auto_20210709_1324'),
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.candidato')),
                ('votante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votantes.votantes', unique=True)),
            ],
            options={
                'verbose_name': 'eleccion',
                'verbose_name_plural': 'elecciones',
                'unique_together': {('candidato', 'votante')},
            },
        ),
    ]
