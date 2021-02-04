from django.shortcuts import render
from django.http import HttpResponse
from .models import Ksiazki, Kategorie


def index(request):
    wszystkie = Ksiazki.objects.all()
    kategorie = Kategorie.objects.all()

 #   jeden = Ksiazki.objects.get(pk=2)
 #   kat = Ksiazki.objects.filter(kategoria=3
 #   null = Ksiazki.objects.filter(kategoria__isnull=True
 #   kat_name = Kategorie.objects.get(id=1)
    return HttpResponse(Ksiazki.objects.all()) # w nawiasach co chcemy, np. return HttpResponse(jeden)

def kategoria(request, id):
    kategoria_user = Kategorie.objects.get(pk=id)
    return HttpResponse(kategoria_user.kategoria)

def ksiazka(request, id):
    ksiazka_user = Ksiazki.objects.get(pk=id)
    napis = "<h1>" + str(ksiazka_user) + "</h1>" + \
            "<p>" + str(ksiazka_user.opis) + "</p>" + \
            "<p>" + str(ksiazka_user.cena) + "</p>"
    return HttpResponse(napis)



