from django.db import models
from django.core.validators import RegexValidator

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade_escolha = (
        ('clino geral', 'clinico geral'),
        ('pediatra', 'pediatra'),
        ('psiquiatria', 'psiquiatria'),
        ('CAR', 'car'),
    )
    especialidade = models.CharField(max_length=30, choices=especialidade_escolha)
    crm = models.CharField(max_length=8, unique=True,
        validators=[RegexValidator(r'^\d{2}/\d{5}$')],                 
        )
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    status_escolha = (
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado')
    )
    status = models.CharField(max_length=30, choices=status_escolha)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE) #chave estrangeira de medico
    REQUIRED_FIELDS = ['paciente', 'data', 'medico']

    def __str__(self):
        return f"Consulta com {self.medico.nome} - {self.paciente}"
