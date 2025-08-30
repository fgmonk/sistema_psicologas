from django import forms
from .models import Paciente
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator




class PacienteForm(forms.ModelForm):
    rut = forms.CharField(
        max_length=12
      
    )

    class Meta:
        model = Paciente
        fields = '__all__'
