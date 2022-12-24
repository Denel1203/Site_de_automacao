from django.forms import ModelForm
from .models import Envio
from django.core.mail import EmailMessage

class EnviarForm(ModelForm):
    class Meta:
        model = Envio
        fields = ['Name', 'Email', 'Message', 'type']

    
    def send_email(self):
        Name = self.cleaned_data['Name']
        Email = self.cleaned_data['Email']
        Message = self.cleaned_data['Message']
        type = self.cleaned_data['type']

        mail = EmailMessage(
            subject = type,
            from_email = '',
            to = [Email,],
            body = Message,
            headers={
                'Replsy-To' : ''
            }
        )
        mail.send()