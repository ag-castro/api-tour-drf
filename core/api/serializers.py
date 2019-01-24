from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico, DocIdentificacao
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    doc_id = DocIdentificacaoSerializer()

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()
        return ponto

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'status', 'descricacao', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco', 'foto', 'doc_id')
        ready_only_fields = ('comentarios', 'avaliacoes')
