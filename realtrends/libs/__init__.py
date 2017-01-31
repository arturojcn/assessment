"""
    realtrends.libs
"""
from .meli import Meli
from django.conf import settings

#Configuracion API Mercadolibre
meli = Meli(client_id=settings.MELI_APP_ID, client_secret=settings.MELI_APP_SECRET_KEY)
meli_auth_url = meli.auth_url(redirect_URI=settings.MELI_APP_CALLBACK)