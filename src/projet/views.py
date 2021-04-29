#from django.http import HttpResponse
from django.shortcuts import render 
     


def Accueil(request):
    return render(request, "accueil.html")



def Produit(request):
    return render(request, "produit.html")



def Contact(request):
    return render(request, "contact.html")



def Blog(request):
    return render(request, "blog.html")

#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj