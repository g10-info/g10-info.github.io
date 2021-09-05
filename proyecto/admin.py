from django.contrib import admin

# Register your models here.



from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta, Partida

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'autor', 'tipo_categoria')

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'opcion', 'puntaje')

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'resultado')

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Partida, PartidaAdmin)
