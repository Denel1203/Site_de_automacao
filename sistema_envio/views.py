from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EnviarForm
from .models import Envio



def enviar(request):
    form = EnviarForm()
    return render(request, 'sistema_envio/enviar.html', {'form': form})

