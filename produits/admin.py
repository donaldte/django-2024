from django.contrib import admin
from .models import Produit 

#admin.site.register(Produit)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description', 'image')