from django.shortcuts import render
from django.http import HttpResponse
from .models import TCA, AC

def menutca(request):
    return render(request, 'menu.html')

def cadastrartca(request):
    if request.method == "GET":
        return render(request, 'formTca.html')
    
    elif request.method == "POST":

        tcaNum = request.POST.get("tcaNUM")
        razaoSocial = request.POST.get("razaoSocial")
        endereco = request.POST.get("endereco")
        email = request.POST.get("email")
        cpfcnpj = request.POST.get("cpfcnpj")

        newTCA = TCA.objects.filter(cpfcnpj=cpfcnpj)

        if newTCA.exists(): #retorno se cpfcnpj ja existe
            return render(request, 'formtca.html', {'tcaNum':tcaNum, 'razaoSocial':razaoSocial, 'endereco':endereco, 'email':email })

        newTCA = TCA(
            tcaNum = tcaNum,
            razaoSocial = razaoSocial,
            endereco = endereco,
            email = email,
            cpfcnpj = cpfcnpj
        )

        newTCA.save()

        return render(request, 'formtca.html')

def listartca(request):
    if request.method == "GET":
        tcas = TCA.objects.all()
        return render(request, 'listartca.html', {'tcas': tcas})