# Generated by Django 3.2.2 on 2022-10-14 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0002_candidato_tipo_candidato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleccion',
            name='candidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleccion_to_candidate', to='candidatos.candidato'),
        ),
    ]
