from django import forms
from .models import Votantes

class VerificarVotanteForm(forms.ModelForm):
    class Meta:
        model = Votantes
        fields = ("cedula",)
