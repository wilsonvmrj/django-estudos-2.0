from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Ola mundo !")

def hello(request):
    return render(request,'index.html')


def articles(request,year):
    return HttpResponse("O nao passado foi {ano}".format(ano=year))


def lerClientesBanco(nome):
    lista_nomes = [
        {'nome':'Ana', 'idade':20},
        {'nome':'Pedro','idade':25},
        {'nome':'Joaquin','idade':27},
    ]
    print("Pessoa: ",nome)
    achada =[]
    for pessoa in lista_nomes: 
        if (pessoa['nome'] == nome):    
            achada=pessoa
    
    if len(achada) == 0:
        achada = {'nome':'Nao encontrado','idade': 0}
    
    return achada


def fname(request,nome):
    pessoa=lerClientesBanco(nome)
    return HttpResponse("Nome: {}, idade: {}".format(pessoa['nome'],pessoa['idade']))


def fname2(request,nome):
    pessoa=lerClientesBanco(nome)
    return render(request,'pessoa.html',{'v_idade': pessoa['idade'], 'v_nome': pessoa['nome']})




