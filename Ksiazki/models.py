from django.db import models


class Autorzy(models.Model):

    def __str__(self):
        return self.Autor

    Autor = models.CharField(max_length=50)
    Publikacje = models.TextField(blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

class Kategorie(models.Model):
    def __str__(self):
        return self.Kategoria

    Kategoria = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Ksiazki(models.Model):

    def __str__(self):
        return self.Tytuł

    kategoria = models.ForeignKey(Kategorie,on_delete=models.CASCADE, null=True)
    autorzy = models.ForeignKey(Autorzy,on_delete=models.CASCADE, null=True)
    Tytuł = models.CharField(max_length=50)
    Opis = models.TextField(blank=True)
    Cena = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Ksiazka"
        verbose_name_plural = "Ksiazki"

