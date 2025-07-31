# informes/forms.py
from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['paciente', 'tipo', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows':10, 'placeholder': 'Escriba el contenido del informe aquí...'}),
        }
