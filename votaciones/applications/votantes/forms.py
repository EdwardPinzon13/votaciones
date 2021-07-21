from django import forms
from django.forms.widgets import TextInput,NumberInput,EmailInput
from .models import Votantes

class VerificarVotanteForm(forms.ModelForm):
    class Meta:
        model = Votantes
        fields = ("cedula","email")
        widgets = {
            'cedula': NumberInput(attrs={'placeholder': 'Cédula'}),
            'email':  EmailInput(attrs={'placeholder':'Correo Electrónico','required':True})
        }

