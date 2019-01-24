from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricacao', 'horario_func', 'idade_minima', 'foto')





