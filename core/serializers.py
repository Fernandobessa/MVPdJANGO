from rest_framework import serializers
from .models import Demanda,Peca,Endereco,Contato,Anunciante



class DemandaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id','codigo','url','pecas','enderecos','contatos','anunciantes']
        


class PecaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peca
        fields = ['id','url', 'descricao']


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','url', 'rua','cep','numero']



class ContatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contato
        fields = ['id','url','email','telefone',] 



class AnuncianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anunciante
        fields = ['id','url', 'nome']      

           