from random import randrange

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


@login_required(login_url='/login')
def listar_preguntas(request):
    if request.method == "POST":
        resultado = 0
        for i in range(1, 3):
            resultado += int(request.POST[str(i)])
        Partida.objects.create(usuario=request.user, fecha=timezone.now(), resultado=resultado)
        return redirect("/results")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by('?')[0:2]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            data[item.pregunta] = respuestas
        return render(request, 'proyecto/listar_preguntas.html', {"preguntas": data})



