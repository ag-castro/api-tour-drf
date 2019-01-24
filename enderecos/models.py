from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(
        max_length=150,
        verbose_name='Localização 1'
    )
    linha2 = models.CharField(
        max_length=150,
        verbose_name='Localização 1',
        null=True,
        blank=True,
    )
    cidade = models.CharField(
        max_length=100,
        verbose_name='Cidade'
    )
    estado = models.CharField(
        max_length=50,
        verbose_name='Estado'
    )
    pais = models.CharField(
        max_length=70,
        verbose_name='País'
    )
    latitude = models.IntegerField(
        verbose_name='Latitude',
        null=True,
        blank=True,
    )
    longitude = models.IntegerField(
        verbose_name='Longitude',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.linha1
