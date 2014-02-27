# Create your views here.

from bodeapp.models import *
from django.shortcuts import render
from django.shortcuts import HttpResponse
import django.http

def lista_musicos(request):
    musicos = Musico.objects.all()
    nomes = list()
    for musico in musicos:
        nomes.append(musico.nome)

    #return HttpResponse(nomes)
    return render(request, 'musicos.html', {'lista_musicos': nomes})


