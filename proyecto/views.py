from random import randrange

from django.shortcuts import render
# Create your views here.
'''
def listar_preguntas(request):
    respuestas = Pregunta.objects.order_by("?")
    id = [item.id for item in Pregunta.objects.all()]
    posicion = Pregunta.objects.get(pk=id[randrange(len(id))])
    return render(request, 'proyecto/listar_preguntas.html', {"preguntas" : respuestas} )
'''


from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def listar_preguntas(request):
    contestadas = []
    if request.method == "POST":
        resultado = 0
        for i in range(1, 2):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
            contestadas += opcion.id_pregunta
            Partida.objects.create(usuario=request.user, fecha=datetime.now, resultado=resultado)
        return redirect("/")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by('?')[0:2]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            data[item.pregunta]= respuestas
        return render(request, 'proyecto/listar_preguntas.html', {"preguntas":data})

  
