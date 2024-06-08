from django.shortcuts import redirect, render, HttpResponse
from .models import Produit
from compte.models import User
from django.views import View 
from .forms import ProduitForm
from django.contrib import messages

# import permission and group table 
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

def index(request, *args, **kwargs):
    # verifier si l'utilisateur est dans le groupe vendeurs
    # #  verifier si l'utilisateur a la permission suivante modifier_images et retirer la permission
    # permission = Permission.objects.get(codename='modifier_images')
    # user = User.objects.get(email=request.user.email)
    # user.user_permissions.remove(permission)
    # user.save()
    if request.user.groups.filter(name='vendeurs').exists():
        print('L\'utilisateur est dans le groupe vendeurs')
    else:
        print('L\'utilisateur n\'est pas dans le groupe vendeurs')
    
    # verifier si l'utilisateur a la permission suivante modifier_images
    if request.user.has_perm('produits.modifier_images'):
        print('L\'utilisateur a la permission de modifier les images')
    else:
        print('L\'utilisateur n\'a pas la permission de modifier les images')   
        
    # verifier si l'utilisateur a la liste des permissions create_product, modifier_product et delete_product 
    # avec le has_perms
    if request.user.has_perms(['produits.create_product', 'produits.modifier_product', 'produits.delete_product']):
        print('L\'utilisateur a la liste des permissions create_product, modifier_product et delete_product')
    else:
        print('L\'utilisateur n\'a pas la liste des permissions create_product, modifier_product et delete_product')
    
    
    # donner la permission modifier_images à l'utilisateur
    permission = Permission.objects.get(codename='modifier_images')
    user = User.objects.get(email=request.user.email)
    user.user_permissions.add(permission)
    user.save()
    
    # ajouter un utilisateur à un groupe
    group = Group.objects.get(name='vendeurs')
    user = User.objects.get(email=request.user.email)
    user.groups.add(group)
    user.save()
    
    # creer un groupe 
    group_2, _obj = Group.objects.get_or_create(name='acheteurs') #(object, created)
    
    # content type 
    content_type = ContentType.objects.get_for_model(Produit)
    
    # creer une permission
    permission_2, _ = Permission.objects.get_or_create(codename='acheter_product', name='Peut acheter les produits', content_type=content_type)
    
    # assigner la permission au groupe acheteurs
    group_2.permissions.add(permission_2)
    
    # ajouter l'utilisateur à un groupe
    user.groups.add(group_2)
    user.save()
    
    # verifier si l'utilisateur est dans le groupe acheteurs
    if request.user.groups.filter(name='acheteurs').exists():
        print('L\'utilisateur est dans le groupe acheteurs')
    else:
        print('L\'utilisateur n\'est pas dans le groupe acheteurs')
    
    
    if request.user.has_perm('produits.modifier_images'):
        print('L\'utilisateur a la permission de modifier les images')
    else:
        print('L\'utilisateur n\'a pas la permission de modifier les images') 
        
    liste_produits = Produit.objects.all() # Product.abdou.all()
    context = {
            'produits': liste_produits,
            'nom': 'Produits de la boutique donald',
        }
    return render(request, 'index.html', context)



# class CreateProduct(View):
    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'produits/create_product.html')
    
#     def post(self, request, *args, **kwargs):
#         try:
#             nom = request.POST.get('nom')
#             description = request.POST.get('description')
#             prix = request.POST.get('prix')
#             image = request.FILES.get('image')
            
#             produit = Produit.objects.create(nom=nom, description=description, prix=prix, image=image)
            
#             if produit:
#                 return HttpResponse('Produit enregistré avec succès')
#         except Exception as e:
#             return HttpResponse('Erreur lors de l\'enregistrement du produit')


class CreateProduct(View):
    
    def get(self, request, *args, **kwargs):
        form = ProduitForm()
        return render(request, 'produits/create_product.html', {'form': form})
    
    
    def post(self, request, *args, **kwargs):
        
        form = ProduitForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit enregistré avec succès')
            return redirect('produits:index')
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du produit')
            return render(request, 'produits/create_product.html', {'form': form})