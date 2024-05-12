
from django.urls import path,include
from . import views
from .views import CategoryAPIView, ProduitAPIView

urlpatterns = [
path('', views.index , name='index'),
path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
path('nouvCde/',views.nouveauCommande,name='nouveauCde'),
path('nouvProduit/',views.listProduit,name='liste'),
path('register/', views.register, name='register'),
path('api/category/', CategoryAPIView.as_view()),
path('api/produit/', ProduitAPIView.as_view()),

]