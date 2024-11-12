from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Doador,Material,Denuncia
from django.contrib import messages


def buscacep(request):
    print('teste BUSCA CEP AQUIIIIIII------')


def doador(request):

    if request.method == "GET":

        #Ao fazer o GET antes de renderizar buscar o materiais já cadastrados
        material_list = Material.objects.all()
        #.all trouxe todos dados da Model(tabela) Material

        return render(request,'doador.html',{'material_list':material_list})
    
    elif request.method =="POST":
        cep = request.POST.get('cep')
        logradouro = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        tipo_barulho = request.POST.get('tipo_barulho')


        doador = Denuncia(
            cep = cep,
            logradouro = logradouro,
            cidade = cidade,
            estado = estado,    
            tipo_barulho = tipo_barulho
        )
        doador.save()
        
        return HttpResponse("INSERIDO OK!") #render(request,'')


def PesquisaMaterial(request):
    print('teste')
    return JsonResponse({"teste":1})