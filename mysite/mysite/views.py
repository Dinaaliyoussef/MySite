from django.shortcuts import render
from django.template import loader

def index(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html',context)

