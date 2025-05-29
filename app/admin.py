from django.contrib import admin
from .models import *

# ========== INLINES ==========

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicaoEnsino', 'turma', 'data_inicio', 'data_previsao_termino']
    list_filter = ['curso', 'instituicaoEnsino', 'turma']
    search_fields = ['pessoa__nome', 'curso__nome']

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoAreaSaberInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class InstituicaoEnsinoInline(admin.TabularInline):
    model = InstituicaoEnsino
    extra = 1


# ========== ADMIN ==========

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]
    
@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    pass

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaSaberInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [InstituicaoEnsinoInline]

@admin.register(AvaliacaoTipo)
class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicaoEnsino', 'turma', 'data_inicio', 'data_previsao_termino']
    list_filter = ['curso', 'instituicaoEnsino', 'turma']
    search_fields = ['pessoa__nome', 'curso__nome']

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
    list_display = ['disciplina', 'curso']
