from django import forms
from django.forms.widgets import TextInput
from .models import Votantes

class VerificarVotanteForm(forms.ModelForm):
    class Meta:
        model = Votantes
        fields = ("cedula",)
        widgets = {
            'cedula': TextInput(attrs={'placeholder': 'Cédula'}),
        }
        
