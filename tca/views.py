from django.shortcuts import render
from django.http import HttpResponse

def tca(request):
    if request.method == "GET":
        return render(request, 'tca.html')
    elif request.method == "POST":
        tcaNum = request.POST.get("numTCA")
        razaoSocial = request.POST.get("razaoSocial")
        endereco = request.POST.get("endereco")
        email = request.POST.get("email")
        cpfcnpj = request.POST.get("cpfcnpj")

        print(razaoSocial)
        print(endereco)
        print(cpfcnpj)
        return HttpResponse('Teste')
