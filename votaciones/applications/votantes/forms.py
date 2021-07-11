from django import forms
from django.forms.widgets import TextInput,NumberInput
from .models import Votantes

class VerificarVotanteForm(forms.ModelForm):
    class Meta:
        model = Votantes
        fields = ("cedula",)
        widgets = {
            'cedula': NumberInput(attrs={'placeholder': 'Cédula'}),
        }

