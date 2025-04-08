from django.shortcuts import render
from requests import Response
from .serializers import ServicoSerializer
from .models import Servico, Agendamento
from rest_framework.decorators import api_view

@api_view(['GET']) #listar informações
def read_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True) #nome da variavel que criamos
    return Response(serializer.data) #data -> dados



