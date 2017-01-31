"""
    realtreand.core.forms
    Formularios
"""
from django import forms
from .models import ProductsCategory

#https://api.mercadolibre.com/categories/MLV1747/listing_types 
LISTING_TYPES = (
    ('bronze', 'Clasico'),
    ('silver', 'Plata'),
)

CONDITION_TYPES = (
    ('new', 'Nuevo'),
    ('use', 'usado'),
)

#https://api.mercadolibre.com/categories/MLV1747 - settings - buying_modes
BUYING_MODES = (
    ('auction', 'auction'),
    ('buy_it_now', 'buy_it_now'),
)

class ProductForm(forms.Form):
    """
        Formulario Produdcto
    """
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Titulo',
        max_length=100,
        help_text='Ej.: Camisa Lacoste Hombre Manga Larga'
    )
    subtitle = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Sub Titulo',
        max_length=100,
        help_text='coloque un subtitulos para su producto'
    )
    listing_type_id = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo',
        choices=LISTING_TYPES,
        initial='silver',
        help_text='seleccione un tipo para su producto'
    )
    condition = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Condicion',
        choices=CONDITION_TYPES,
        initial='new',
        help_text='seleccione la condicion de su producto'
    )
    buying_mode = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Metodo de pago',
        choices=BUYING_MODES,
        initial='buy_it_now',
        help_text='Ingrese su metodo de pago'
    )
    category_id = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=ProductsCategory.objects.all(),
        label='Categoria',
        initial='1',
        help_text='Seleccione la categoria para su producto'
    )
    description = forms.CharField(
        label='Descripcion',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text='Escribe tu descripcion...'
    )
    available_quantity = forms.IntegerField(
        label='Cantidad Disponible',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text='Cantidad Disponible en stock'
    )
    price = forms.IntegerField(
        label='Precio',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text='Indique el precio para producto'
    )
