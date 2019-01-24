from django.db import models


class Atracao(models.Model):
    nome = models.CharField(
        max_length=150,
        verbose_name='Atração',
        help_text='Nome da Atração'
    )
    descricacao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição da atração'
    )
    horario_func = models.TextField(
        verbose_name='Horário de Funcionamento',
    )
    idade_minima = models.IntegerField(
        verbose_name='Idade Miníma'
    )
    foto = models.ImageField(
        upload_to='atracoes',
        null=True,
        blank=True
    )
    observacoes = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome

