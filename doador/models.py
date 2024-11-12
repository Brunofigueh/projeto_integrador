from django.db import models

# Create your BANCO DE DADOS here

class Doador(models.Model):
    nome = models.CharField(max_length=50, default=0)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.nome
    
class Material(models.Model):
    tipo_material = models.CharField(max_length=50)
    unidade_material = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    doador = models.ForeignKey(Doador, blank=True, null=True,on_delete=models.SET_NULL)
    doacoes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.tipo_material
    

class Denuncia(models.Model):
    cep = models.CharField(max_length=8, default=0)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    tipo_barulho = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome