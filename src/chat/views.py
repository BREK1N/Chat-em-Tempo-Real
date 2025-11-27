from django.shortcuts import render

def sala(request, nome_sala):
    return render(request, 'chat/sala.html', {
        'nome_sala': nome_sala
    })
