"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # Tabelas principais
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicoesEnsinoView.as_view(), name='instituicoes'),
    path('areas-saber/', AreasSaberView.as_view(), name='areas_saber'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
]
