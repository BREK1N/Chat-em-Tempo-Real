from django.shortcuts import render
from .models import Mensagem

def sala(request, nome_sala):
    mensagens = Mensagem.objects.filter(sala=nome_sala).order_by('timestamp')

    return render(request, 'chat/sala.html', {
        'nome_sala': nome_sala,
        'mensagens': mensagens,
    })
