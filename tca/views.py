from django.shortcuts import render
from django.http import HttpResponse

def tca(request):

    return render(request, 'tca.html')