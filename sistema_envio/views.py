from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EnviarForm
from django.contrib import messages



def enviar(request):
    if request.method == 'POST':
        form = EnviarForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Email enviado com sucesso.')
            form = EnviarForm()
                    
        else:
            messages.erro(request, "Nao foi possivel enviar o email")
    else:
        form = EnviarForm()
    context =  {
        "form": form
    }
    return render(request, 'sistema_envio/enviar.html',{"form": form})
def mostrar(request):
    return render(request, 'sistema_envio/mos.html')
