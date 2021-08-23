from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_preguntas, name='listar_preguntas'),
]
