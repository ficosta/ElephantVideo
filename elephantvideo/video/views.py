from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import datetime

# Create your views here.
def lista_canais(request):
    channels = Channel.objects.all()
    return render(request, 'video/lista_canais.html', {'title': 'Lista de Canais','channels':channels})

def video(request, channel=None, date=None, time=None):
    if channel == None:
        HttpResponseRedirect(reverse('video:lista_canais'))
    else:
        if request.method == 'POST':
            #Efetua a busca com data e Hora
            date=request.POST.get('date')
            time = request.POST.get('time')

            diaHora= datetime.strptime(('{} {}'.format(date,time)), "%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M:%S")
            print(diaHora)
            clip = Clip.objects.filter(channel__slug=channel,recordDate__lte=diaHora).order_by('-recordDate').first()
        else:
            clip = Clip.objects.filter(channel__slug=channel).order_by('-recordDate').first()
    print(request)
    return render(request, 'video/video.html', {'title': 'Player','clip':clip,'date':date,'time':time})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'video/companies.html', {'title':"Administrar Empresas",'companies': companies})

def channels(request):
    channels = Channel.objects.all()
    return render(request, 'video/channels.html', {'title':"Administrar Canais",'channels': channels})
