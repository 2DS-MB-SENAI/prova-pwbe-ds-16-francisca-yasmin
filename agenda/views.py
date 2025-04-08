from django.shortcuts import render
from requests import Response
from .serializers import ServicoSerializer
from .models import Servico, Agendamento
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET']) #listar informações
def read_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True) #nome da variavel que criamos
    return Response(serializer.data) #data -> dados

@api_view(['POST'])
def create_servicos(request):
     if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data, many=True) #converter o JSON para carro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) #pegar informações de serviços oferecidos
def pegar_servico(request, pk):
    try:
        servicos = Servico.objects.get(pk = pk)
    except Servico.DoesNotExist:
        return Response({'erro': ' serviço inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServicoSerializer(servicos)
    return Response(serializer.data)

