from django.db import models

class Mensagem(models.Model):
    sala = models.CharField(max_length=255)
    conteudo = models.TextField()
    # Por enquanto, vou salvar o nome como texto para simplificar
    autor = models.CharField(max_length=255, default="Anônimo")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.conteudo} ({self.sala})"
