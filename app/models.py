from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class UF(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla
    class Meta:
        verbose_name = "UF"   
        verbose_name_plural = "USs"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name="UF")  # <-- mudar para FK

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"   
        verbose_name_plural = "Cidades"



class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(verbose_name="Pai")
    mae = models.CharField(verbose_name="Mãe")
    cpf = models.CharField(verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE,verbose_name="Ocupacao")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituicao de Ensino")
    site = models.CharField(verbose_name="Site")
    telefone = models.CharField(verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "InstituicaoEnsino"
        verbose_name_plural = "InstituicaoEnsinos"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreaSaberes"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária")
    duracao_meses = models.IntegerField(verbose_name="Duração em meses")
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="AreaSaber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição", null=True, blank=True)


    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE,verbose_name="AreaSaber")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicaoEnsino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="InstituicaoEnsino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name="Turma")  # <-- adiciona FK turma
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    def __str__(self):
        return f"{self.pessoa}, {self.curso}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo da avaliação")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "AvaliacaoTipo"
        verbose_name_plural = "AvaliacaoTipos"

class Avaliacao(models.Model):
    descricao = models.CharField(verbose_name="Descricao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    avaliacaoTipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE,verbose_name="AvaliacaoTipo")
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Numero de Faltas")
    def __str__(self):
        return f"{self.pessoa}, {self.numero_faltas}"
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Turno")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Ocorrencia(models.Model):
    descricao = models.CharField(verbose_name="Descricao")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Dsciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa")
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.disciplina.nome)

    class Meta:
        verbose_name = "CursoDisciplina"
        verbose_name_plural = "CursoDisciplinas"





