from django.shortcuts import render
from .models import Servico, Agendamento

@api_view(['GET'])
def read_servicos(request):
    servicos =1