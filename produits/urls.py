from django.urls import path 
from .views import index, CreateProduct

app_name = 'produits'

urlpatterns = [
    path('', index, name='index'),
    path('create-produit/', CreateProduct.as_view(), name='create_product'),
]