from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    comentario = models.TextField(
        verbose_name='Comentário',
    )
    data = models.DateTimeField(
        verbose_name='Comentado em',
        auto_now_add=True
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Aprovado',
        help_text='Selecione para exibir este comentário'
    )

    def __str__(self):
        return self.usuario.first_name
