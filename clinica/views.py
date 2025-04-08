from django.shortcuts import get_object_or_404, redirect, render
from clinica.forms import ConsultaForm
from .models import Consulta, Medico

#listar os medicos e filtrar por especialiade
def listar_medicos(request):
    medicos = Medico.objects.all()
    especialidade = request.GET.get('especialidade')
    if especialidade:
           medicos = medicos.filter(especialidade=especialidade)

    pesquisa = request.GET.get('search', '')  
    if pesquisa:
        medicos = Medico.objects.filter(especialidade__icontains=pesquisa)
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

#criar consulta
def criar_consulta(request):
    if request.method == 'POST':
        consultas = ConsultaForm(request.POST)
        if consultas.is_valid():
            consultas.save()
            return redirect('listar_medicos')
    else:
        consultas = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'consulta': consultas})

#mostrar detalhes da consulta por id
def detalhes_consulta(request, id):
    consultas = get_object_or_404(Consulta, id = id)    
    consultas.objects.filter(id)
    return render(request, 'clinica/detalhes_consulta.html', {'consultas': consultas})




