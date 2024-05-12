from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome To My First Game ")
# Create your views here.
