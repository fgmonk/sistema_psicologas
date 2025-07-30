from django import forms
from .models import Sesion

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['paciente', 'fecha', 'hora', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
