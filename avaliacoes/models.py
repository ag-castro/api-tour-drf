from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    comentario = models.TextField(
        verbose_name='Comentário',
        null=True,
        blank=True
    )
    nota = models.DecimalField(
        verbose_name='Nota de Avaliação',
        max_digits=3,
        decimal_places=2
    )
    data = models.DateTimeField(
        verbose_name='Avaliado em',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.usuario.first_name


