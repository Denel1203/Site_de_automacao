from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnviarForm



def enviar(request):
    if request.method == 'POST':
        form = EnviarForm(request.POST)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            form.send_email()
            form= EnviarForm()

        def send_email(self):
            nome = self.cleaned_data['Name']
            email = self.cleaned_data['Email']
            message = self.cleaned_data['Message']
            subject = self.cleaned_data['Subject']

        mail = EmailMessage(
            subject=subject,
            from_email= None,
            to=[email,],
            body=message
        )

        mail.send()
    else:
        form = EnviarForm()
   
    return render(request, 'sistema_envio/enviar.html', {"form":})

