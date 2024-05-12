from django.db import models
from datetime import date
# Create your models here.
TYPE_CHOICES=[
('em','emballé'),
('fr','Frais'),
('cs','Conserve')]
TYPE_CHOICES=[
('AI' , 'Alimentaire'), ('Mb','Meuble'),
('Sn','Sanitaire'), ('Vs','Vaisselle'),
('V','Vêtement'),('Jx','Jouets'),
('L','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]    
# Class Categories : 
class Categorie (models.Model) :
    name = models.CharField(max_length = 50 ,choices=TYPE_CHOICES, default = 'Alimentaire')
    def __str__(self) :
        return "le nom est :"+self.name
# Class Fournisseur : 
class Fournisseur (models.Model) :
    nom = models.CharField(max_length = 100)
    adresse = models.TextField()
    email= models.EmailField()
    telephone = models.CharField(max_length = 8)
    def __str__(self) :
        return self.nom+""+self.adresse+""+self.email+""+self.telephone
# Class Produits : 
class Produit(models.Model) :
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non definie')
    prix = models.DecimalField(max_digits=10 , decimal_places=3)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES,default='em')
    Img = models.ImageField(blank=True)
    Catégorie = models.ForeignKey(Categorie , on_delete = models.CASCADE,null = True)
    frs = models.ForeignKey(Fournisseur ,on_delete=models.CASCADE,null=True )
    def __str__(self) :
        return self.libelle+""+self.description+""+str(self.prix)+""+self.type+""+str(self.Img)
# Class ProduitNC : 
class ProduitNC(Produit) : 
    duree_garantie = models.CharField(max_length = 100)
    def __str__(self) :
        return ""+self.duree_garantie
# Class Commande : 
class Commande (models.Model) :
    dateCde = models.DateField(null = True , default = date.today)
    totalCde = models.DecimalField(max_digits = 10 , decimal_places = 3)
    produits = models.ManyToManyField(Produit)
    def __str__(self) :
        return ""+str(self.dateCde)+"total :"+str(self.totalCde)+"p :"+str(self.produits)
    def calc(self) : 
        return sum(Produit.prix for Produit in self.produits.all())


