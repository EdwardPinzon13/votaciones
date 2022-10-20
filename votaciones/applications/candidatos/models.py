from django.db import models
from applications.votantes.models import Votantes,tipo_candidato
from model_utils.models import TimeStampedModel
# Create your models here.


class Candidato(models.Model):
    nombre  = models.CharField(max_length=100)
    apellido  = models.CharField(max_length=100, null=True)
    cargo  = models.CharField(max_length=100,null=True)
    dependencia = models.CharField(max_length=100,null=True)
    foto = models.ImageField(("Foto Candidato"), upload_to='candidatos')
    tipo_candidato = models.ForeignKey(tipo_candidato, on_delete=models.CASCADE, related_name = 'candidate_tipo_candidato')

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.nombre + ' - ' + self.apellido + ' - ' + self.cargo + ' - ' + self.dependencia

class eleccion(TimeStampedModel):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE,related_name='eleccion_to_candidate')
    votante = models.ForeignKey(Votantes,on_delete=models.CASCADE,unique=True)

    class Meta:
        verbose_name = "eleccion"
        verbose_name_plural = "elecciones"
        unique_together = ['candidato','votante']

    def __str__(self):
        return self.votante.nombre + ' - ' + str(self.votante.email) + ' - ' + str(self.votante.estado_voto)
