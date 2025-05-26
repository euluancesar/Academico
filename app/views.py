from django.shortcuts import render
from django.views import View
from .models import (
    Pessoa, Cidade, Ocupacao, InstituicaoEnsino, AreaSaber, Curso, Turma,
    Disciplina, Matricula, Frequencia, AvaliacaoTipo, Avaliacao, Turno,
    Ocorrencia, CursoDisciplina
)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})

class InstituicoesEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'areas_saber.html', {'areas': areas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

class AvaliacaoTiposView(View):
    def get(self, request, *args, **kwargs):
        tipos = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacao_tipos.html', {'tipos': tipos})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class CursoDisciplinasView(View):
    def get(self, request, *args, **kwargs):
        cursodisciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplinas.html', {'cursodisciplinas': cursodisciplinas})
