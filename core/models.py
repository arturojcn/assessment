from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductsCategory(models.Model):
    """
        Model: MeliProfile
        Descripcion: Categorias de productos en Mercadolibre
        Doc: https://api.mercadolibre.com/sites/MLV/categories
    """
    category_id = models.CharField(max_length=7, blank=True, null=True, unique=True)
    name = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __unicode__(self):
        return self.name
        