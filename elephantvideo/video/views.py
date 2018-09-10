from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def lista_canais(request):
    channels = Channel.objects.all()
    return render(request, 'video/lista_canais.html', {'title': 'Lista de Canais','channels':channels})

def video(request, channel, day,year,month,hour,minute):
    channels = Channel.objects.all()
    return render(request, 'video/video.html', {'title': 'BAND'})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'video/companies.html', {'title':"Administrar Empresas",'companies': companies})

def channels(request):
    channels = Channel.objects.all()
    return render(request, 'video/channels.html', {'title':"Administrar Canais",'channels': channels})

def busca(request):
    return HttpResponseRedirect(reverse('globo/12/12/1222/12/22/'))
