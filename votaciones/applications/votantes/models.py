from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{5,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class tipo_candidato(models.Model):
    type_candidate = models.CharField('Tipo de candidato', max_length=30)
class Votantes(models.Model):
    cedula = models.CharField("Numero de identificación", validators=[phone_regex], max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido  = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    estado_voto = models.BooleanField(default=False)
    tipo_candidato = models.ForeignKey(tipo_candidato, on_delete=models.CASCADE, related_name = 'votante_tipo_candidato')

    class Meta:
        verbose_name = "Votante"
        verbose_name_plural = "Votantes"

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.cedula





