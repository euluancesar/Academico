from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_do_pai = models.IntegerField(verbose_name="Nome do pai")
    nome_da_mae = models.IntegerField(verbose_name="Nome da mãe")
    cpf = models.IntegerField(verbose_name="CPF")
    data_nasc = models.IntegerField(verbose_name="Data de nascimento")
    email = models.IntegerField(verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE,verbose_name="Ocupacao")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


