from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import AtracoesSerializer
from atracoes.models import Atracao


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome', 'descricacao')
