from django.contrib import admin
from .models import *

# ========== INLINES ==========

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicaoEnsino', 'turma', 'data_inicio', 'data_previsao_termino']
    list_filter = ['curso', 'instituicaoEnsino', 'turma']
    search_fields = ['pessoa__nome', 'curso__nome']


# i) Ocupação e pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

# ii) Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

# iii) Área do saber e cursos
class CursoAreaSaberInline(admin.TabularInline):
    model = Curso
    extra = 1

# iv) Cursos e disciplinas
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

# vi) Turmas e alunos
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

# vii) UF e cidades
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

# ix) Estudantes, disciplinas, avaliações, frequência
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

# ========== ADMIN ==========

# i) Ocupação e pessoas
@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# ii) Instituição e cursos
@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

# iii) Área do saber e cursos
@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaSaberInline]

# iv) Cursos e disciplinas
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# v) Disciplinas e avaliações
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# vi) Turmas e alunos
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]

# vii) UF e cidades
@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

# ix) Estudantes, disciplinas, avaliações, frequência
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

# Admins simples
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(AvaliacaoTipo)
class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicaoEnsino', 'turma', 'data_inicio', 'data_previsao_termino']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'curso', 'disciplina', 'avaliacaoTipo']

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'disciplina', 'numero_faltas']

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data', 'pessoa', 'curso', 'disciplina']

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['nome']

# @admin.register(Ocorrencia)
# class OcorrenciaAdmin(admin.ModelAdmin):
#     list_display = ['id']

@admin.register(CursoDisciplina)
class CursoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'disciplina']
