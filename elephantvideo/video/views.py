from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def lista_canais(request):
    channels = Channel.objects.all()
    return render(request, 'video/lista_canais.html', {'title': 'Lista de Canais','channels':channels})

def video(request, channel=None, date=None, hour=None):
    if channel == None:
        HttpResponseRedirect(reverse('video:lista_canais'))
    else:
        if request.method == 'POST':
            #Efetua a busca com data e Hora
            return render(request, 'video/video.html', {'title': 'post'})
        else:
            clip = Clip.objects.filter(channel__slug='REDETVSP')[:1]
            return render(request, 'video/video.html', {'title': 'ultimo video','clip':clip)

def companies(request):
    companies = Company.objects.all()
    return render(request, 'video/companies.html', {'title':"Administrar Empresas",'companies': companies})

def channels(request):
    channels = Channel.objects.all()
    return render(request, 'video/channels.html', {'title':"Administrar Canais",'channels': channels})
