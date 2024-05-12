from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Produit
from .models import Fournisseur
from .forms import Commande
from .forms import CommandeForm
from django.shortcuts import redirect
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer
from rest_framework import viewsets
# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required
def index(request):
   list=Produit.objects.all()
   return render(request,'magasin/vitrine.html',{'list':list})
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Coucou {username}, Votre compte a été créé avec succès !")
            return redirect("index")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})



def listProduit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})

def nouveauFournisseur(request):
    form = FournisseurForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    fournisseurs = Fournisseur.objects.all()

    context = {'form': form, 'fournisseurs': fournisseurs}
    return render(request, 'magasin/fournisseur.html', context)        
def nouveauCommande(request):
    form = CommandeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    commandes = Commande.objects.all()

    context = {'form': form, 'commandes': commandes}
    return render(request, 'magasin/Commande.html', context)        

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        Produits = Produit.objects.all()
        serializer = ProduitSerializer(Produits, many=True)
        return Response(serializer.data)
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(Catégorie_id=category_id)
        return queryset