"""
    realtrends.authorize.views
"""
import time
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login as auth_login, logout as auth_logout
from realtrends.libs import meli_auth_url, meli
from .models import MeliProfile
# Create your views here.

def index(request):
    """Authorize Index"""
    print meli_auth_url
    return render(request, 'authorize/index.html', {})

def login(request):
    """Authorize login"""
    return redirect(meli_auth_url)

def authorized(request):
    """Authorize authorized"""
    code = request.GET.get('code', None)
    if code:
        meli.authorize(code, 'http://localhost:8000/auth/authorized')
        params = {'access_token' : meli.access_token}
        response = meli.get(path="/users/me", params=params)
       
        json_data = response.json()
        meli_id = json_data.get('id')
        nickname = json_data.get('nickname')
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        email = json_data.get('email')

        meli_profile, new_profile = MeliProfile.objects.get_or_create(
            meli_id=meli_id,
            nickname=nickname,
            first_name=first_name,
            last_name=last_name,
            email=email)
        auth_login(request, meli_profile.user)
        request.session['meli_id'] = meli_id
        request.session['access_token'] = meli.access_token
        request.session['refresh_token'] = meli.refresh_token
        request.session['expires_in'] = time.time() + 21600
        return redirect('/')

    raise Http404('Pagina no encontrada')

def logout(request):
    """Cerrar Sesion"""
    try:
        auth_logout(request)
        del request.session['access_token']
    except KeyError:
        pass
    return redirect('/')