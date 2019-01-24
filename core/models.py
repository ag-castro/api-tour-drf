from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from enderecos.models import Endereco


class DocIdentificacao(models.Model):
    descricao = models.CharField(
        max_length=100
    )


class PontoTuristico(models.Model):
    nome = models.CharField(
        max_length=150,
        verbose_name='Ponto Turístico',
        help_text='Nome do ponto turístico'
    )
    descricacao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição do ponto turístico'
    )
    status = models.BooleanField(
        verbose_name='Publicado',
        help_text='Selecione para ativar este ponto turístico',
        default=False
    )
    atracoes = models.ManyToManyField(
        Atracao,
        verbose_name='Atrações'
    )
    comentarios = models.ManyToManyField(
            Comentario,
            verbose_name='Comentários'
    )
    avaliacoes = models.ManyToManyField(
        Avaliacao,
        verbose_name='Avaliações'
    )
    endereco = models.ForeignKey(
        Endereco,
        verbose_name='Endereço',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    foto = models.ImageField(
        upload_to='pontos_turisticos',
        null=True,
        blank=True
    )
    doc_id = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE,
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'

    def __str__(self):
        return self.nome

