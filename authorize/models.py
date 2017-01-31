from __future__ import unicode_literals

import os
import base64
from django.db import models
from django.conf import settings
# Create your models here.

class MeliProfile(models.Model):
    """
        Model: MeliProfile
        Descripcion: Perfil de Mercadolibre
    """
    meli_id = models.IntegerField(unique=True,blank=True, null=True)
    nickname = models.CharField(max_length=500, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)

    def __unicode__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        """Validar el guardado a la base de datos"""
        print "enro"
        if not self.pk:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user_existing = User.objects.filter(username=self.nickname)
            if user_existing: # Check if user exists, No implement
                return
            password = base64.b64encode(os.urandom(16))
            user = User.objects.create_user(
                username=self.nickname,
                password=password)

            self.user = user
           
        super(MeliProfile, self).save(*args, **kwargs)
