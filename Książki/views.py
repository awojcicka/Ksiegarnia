from django.shortcuts import render
from django.http import HttpResponse
from .models import Książki, Kategorie


def index(request):
    wszystkie = Książki.objects.all()
    kategorie = Kategorie.objects.all()

 #   jeden = Książki.objects.get(pk=2)
 #   kat = Książki.objects.filter(kategoria=3
 #   null = Książki.objects.filter(kategoria__isnull=True
 #   kat_name = Kategorie.objects.get(id=1)
    return HttpResponse(Książki.objects.all()) # w nawiasach co chcemy, np. return HttpResponse(jeden)

def kategoria(request, id):
    kategoria_user = Kategorie.objects.get(pk=id)
    return HttpResponse(kategoria_user.kategoria)

def ksiazka(request, id):
    książka_user = Książki.objects.get(pk=id)
    napis = "<h1>" + str(książka_user) + "</h1>" + \
            "<p>" + str(książka_user.opis) + "</p>" + \
            "<p>" + str(książka_user.cena) + "</p>"
    return HttpResponse(napis)



