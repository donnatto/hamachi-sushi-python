from django import forms
from .models import Reserva, Postulante, Mensaje


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class FileInput(forms.FileInput):
    input_type = 'file'


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['nombre', 'apellidos', 'fecha', 'hora', 'comensales', 'nroContacto', 'correo']
        labels = {'nombre': 'Nombre', 'apellidos': 'Apellidos', 'fecha': 'Fecha', 'hora': 'Hora',
                  'comensales': 'Nro. de Comensales', 'nroContacto': 'Nro. de Contacto', 'correo': 'Correo Electrónico'}
        widgets = {'fecha': DateInput(), 'hora': TimeInput(), }


class PostulanteForm(forms.ModelForm):

    class Meta:
        model = Postulante
        fields = ['nombre', 'correo', 'nroContacto', 'cv', 'mensaje']
        labels = {'nombre': 'Nombre', 'correo': 'Correo Electrónico', 'nroContacto': 'Nro. de Contacto', 'cv': 'Hoja de Vida', 'mensaje': 'Sobre ti'}
        widgets = {'cv': FileInput()}


class MensajeForm(forms.ModelForm):

    class Meta:
        model = Mensaje
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
        labels = {'nombre': 'Nombre', 'correo': 'Correo Electrónico', 'asunto': 'Asunto', 'mensaje': 'Mensaje'}
