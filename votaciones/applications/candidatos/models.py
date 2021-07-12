from django.db import models
from applications.votantes.models import Votantes
from model_utils.models import TimeStampedModel
# Create your models here.

class Candidato(models.Model):
    nombre  = models.CharField(max_length=100)
    apellido  = models.CharField(max_length=100)
    cargo  = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    foto = models.ImageField(("Foto Candidato"), upload_to='candidatos')

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.cargo

class eleccion(TimeStampedModel):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    votante = models.ForeignKey(Votantes,on_delete=models.CASCADE,unique=True)

    class Meta:
        verbose_name = "eleccion"
        verbose_name_plural = "elecciones"
        unique_together = ['candidato','votante']

    def __str__(self):
        return str(self.candidato.id) + ' ' + self.votante.nombre
