from django import forms
from django.core.mail import EmailMessage


class EnviarForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField(max_length=80)
    Message = forms.CharField(max_length=11)
    Subject = forms.ChoiceField(choices=['noticias', 'consultas', 'exames', 'boletos'])

   