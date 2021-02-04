from django.contrib import admin
from .models import Ksiazki, Autorzy, Kategorie

admin.site.register(Ksiazki)
admin.site.register(Autorzy)
admin.site.register(Kategorie)