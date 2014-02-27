# Create your views here.

from bodeapp.models import *
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q
import django.http

def lista_musicos(request):
    musicos = Musico.objects.all()
    nomes = list()
    for musico in musicos:
        nomes.append(musico.nome)

    #return HttpResponse(nomes)
    return render(request, 'musicos.html', {'lista_musicos': nomes})

def search(request):
    """docstring for search"""
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(titulo__icontains=query)
        )
        results = Disco.objects.filter(qset).distinct()
    else:
        results=[]
    return render(request, 'search.html', {'results': results, 'query': query})

