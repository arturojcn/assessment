import time
from realtrends.libs import Meli
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

class MeliMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated():
            refresh_token = request.session.get('refresh_token', None)
            expires_in = request.session.get('expires_in', None)
            if time.time() > expires_in:
                meli = Meli(
                    client_id=settings.MELI_APP_ID, 
                    client_secret=settings.MELI_APP_SECRET_KEY,
                    access_token=request.session.get('access_token', ''),
                    refresh_token=request.session.get('refresh_token', '')
                )
                try:
                    meli.get_refresh_token()
                    request.session['access_token'] = meli.access_token
                    request.session['refresh_token'] = meli.refresh_token
                    request.session['expires_in'] = time.time() + 21600
                except:
                    logout(request)
                
                

        response = self.get_response(request)

        return response