from django.http import HttpResponse
from django.shortcuts import render
from App.models import *

def inicio(request):
    return HttpResponse("este es el inicio")

def agenda(request):
    agendas= Familia.objects.all()
    #Si quiero listarlo por la terminal, usaria un HttpResponse y usaria lo que esta abajo
    #for agenda in agendas:
        #print(agenda.nombre, agenda.apellido, agenda.email, agenda.cumpleaños, agenda.telefono)
    #return HttpResponse(agenda) 
    return render(request, "app/listar_agenda.html",{'agendas':agendas})
   