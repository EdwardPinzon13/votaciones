from django.contrib import admin

from .models import *



class CandidatoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'cargo',
        'dependencia',
        'tipo_candidato'
    )
    search_fields = ('nombre','apellido')
    

# Register your models here.
admin.site.register(Candidato,CandidatoAdmin)
admin.site.register(eleccion)

