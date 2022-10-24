from django.contrib import admin
from .models import *

# Register your models here.


class VotantesAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombre',
        'apellido',
        'email',
        'estado_voto',
        'tipo_candidato'
    )
    search_fields = ('cedula',)
admin.site.register(Votantes, VotantesAdmin)
admin.site.register(tipo_candidato)


