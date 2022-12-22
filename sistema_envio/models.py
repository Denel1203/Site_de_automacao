from django.db import models


class Envio(models.Model):
    TYPOS = (
        ("NOTICIAS", "NOTICIAS"),
        ("BOLETOS", "BOLETOS"),
        ("CONSULTAS", "CONSULTAS"),
        ("EXAMES", "EXAMES")
    )

    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=80)
    Message = models.CharField(max_length=11)
    type = models.CharField(max_length=15, choices=TYPOS)
