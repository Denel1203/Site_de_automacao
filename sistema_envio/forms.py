from django.forms import ModelForm
from .models import Envio


class EnviarForm(ModelForm):
    class Meta:
        model = Envio
        fields = ['Name', 'Email', 'Message', 'type']

   