"""
    realtrends.core.views
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from realtrends.libs import meli_auth_url, meli
from .forms import ProductForm

# Create your views here.

@login_required
def index(request):
    """Core Index"""
    return render(request, 'core/index.html', {})

@csrf_protect
@login_required
def product(request):
    """Productos View"""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            body = {
                "condition": form.cleaned_data.get("condition"), 
                "warranty":"60 dias", 
                "currency_id":"VEF",
                "description": form.cleaned_data.get("description"), 
                "listing_type_id": form.cleaned_data.get("listing_type_id"), 
                "title": form.cleaned_data.get("title"), 
                "available_quantity": form.cleaned_data.get("available_quantity"), 
                "price": form.cleaned_data.get("price"), 
                "buying_mode": form.cleaned_data.get("buying_mode"), 
                "category_id": form.cleaned_data.get("category_id").category_id, 
                "pictures":[
                    {
                        "source":"https://app.real-trends.com/static/img/rt-iso-small.png"
                    }, 
                    {
                        "source":"https://app.real-trends.com/static/img/rt-iso-small.png"
                    }] 
            }

            response = meli.post("/items", body, {'access_token':meli.access_token})
            new_product = response.json()
            
            if new_product.get('status') and new_product.get('status') == 400:
                messages.error(request, 'Publicacion no registrada')
            else:
                messages.info(request, 'Publicacion Registrada con exito')
                form = ProductForm()

    else:
        form = ProductForm()
    return render(request, 'core/products.html', {'form': form})


@login_required
def list_products(request):
    """Lisado de Publicaciones 'status': 'active',  """
    params = {'access_token' : request.session.get('access_token')}
    response_products = meli.get(
        '/users/{}/items/search'.format(request.session.get('meli_id')),
        params
    )
    items_response = list()
    products = response_products.json()
    list_products = products.get('results', None)
    if list_products:
        search_ids = ','.join(list_products)
        params = {'ids':search_ids, 'access_token' : request.session.get('access_token')}
        items_response = meli.get('/items', params=params)
        items_response = items_response.json()
    else:
        messages.info(request, 'No tiene publicaciones disponibles')
    print items_response
    return render(request, 'core/list_products.html', {'items_response':items_response})