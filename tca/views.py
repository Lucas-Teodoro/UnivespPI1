from django.shortcuts import render
from django.http import HttpResponse
from .models import TCA, AC

def tca(request):
    if request.method == "GET":
        return render(request, 'tca.html')
    
    elif request.method == "POST":

        tcaNum = request.POST.get("tcaNUM")
        razaoSocial = request.POST.get("razaoSocial")
        endereco = request.POST.get("endereco")
        email = request.POST.get("email")
        cpfcnpj = request.POST.get("cpfcnpj")

        newTCA = TCA.objects.filter(cpfcnpj=cpfcnpj)

        if newTCA.exists(): #retorno se cpfcnpj ja existe
            return render(request, 'tca.html', {'tcaNum':tcaNum, 'razaoSocial':razaoSocial, 'endereco':endereco, 'email':email })

        newTCA = TCA(
            tcaNum = tcaNum,
            razaoSocial = razaoSocial,
            endereco = endereco,
            email = email,
            cpfcnpj = cpfcnpj
        )

        newTCA.save()

        return render(request, 'tca.html')
