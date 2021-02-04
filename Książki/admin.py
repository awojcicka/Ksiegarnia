from django.contrib import admin
from .models import Książki, Autorzy, Kategorie

admin.site.register(Książki)
admin.site.register(Autorzy)
admin.site.register(Kategorie)