from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
  return HttpResponse('Hello World')

def companies(request):
  companies = Company.objects.all()
  return render(request, 'companies.html', {'companies': companies})

def channels(request):
  channels = Channel.objects.all()
  return render(request, 'channels.html', {'channels': channels})