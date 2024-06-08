from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nom
    
    # ajouter la permission modifier les images
    class Meta:
        permissions = [
            ("modifier_images", "Peut modifier les images"),
        ]
    
    def get_image_url(self):
        if self.image:
            return self.image.url 
        return None 