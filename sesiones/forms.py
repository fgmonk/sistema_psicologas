from django import forms
from .models import Sesion

# Definimos los motivos de consulta como tuplas (valor, etiqueta)
MOTIVOS_CONSULTA = [
    ('conductual', 'Conductual'),
    ('emocional', 'Emocional'),
    ('academico', 'Académico / Aprendizaje'),
    ('familiar', 'Familiar / Relaciones Familiares'),
    ('social', 'Social / Interacción con pares'),
    ('sueño', 'Trastornos del Sueño'),
    ('alimentacion', 'Trastornos de Alimentación'),
    ('desarrollo', 'Desarrollo / Habilidades'),
]

class SesionForm(forms.ModelForm):
    # Campo motivo de consulta con selección de opciones
    motivo = forms.ChoiceField(choices=MOTIVOS_CONSULTA, label="Motivo de Consulta")
    
    class Meta:
        model = Sesion
        fields = ['paciente', 'fecha', 'hora', 'comentario', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'min': '08:00', 'max': '18:00'}),
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }

    # Validación para excluir fines de semana
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha.weekday() >= 5:  # 5 = sábado, 6 = domingo
            raise forms.ValidationError("No se pueden agendar sesiones en fines de semana.")
        return fecha

class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
