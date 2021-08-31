from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pregunta= models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo_categoria = models.CharField(max_length = 50, default='SOME STRING')

    def __str__(self):
        return self.pregunta


class Respuesta(models.Model):
    id_pregunta= models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    opcion= models.CharField(max_length=500)
    puntaje= models.IntegerField(null=True)


class Partida(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now())
    resultado = models.IntegerField()
    total_preguntas = models.IntegerField(null=True)

