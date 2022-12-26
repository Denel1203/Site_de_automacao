from django.forms import ModelForm
from .models import Envio
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



class EnviarForm(ModelForm):
    class Meta:
        model = Envio
        fields = ['Name', 'Email', 'Message', 'type']

    
    def send_email(self):
        Name = self.cleaned_data['Name']
        Email = self.cleaned_data['Email']
        Message = self.cleaned_data['Message']
        type = self.cleaned_data['type']

        html_content = render_to_string('sistema_envio/mos.html', locals())
        text_content = strip_tags(html_content)

        mail = EmailMultiAlternatives(
            subject = type,
            from_email = '',
            to = [Email,],
            body = Message,
            headers={
                'Replsy-To' : ''
            }
        )
        mail.attach_alternative(html_content, 'text/html')
        mail.send()



