from django.conf.urls import url
from .views import index, product, list_products

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^products/$', product, name='product'),
    url(r'^list_products/$', list_products, name='list_products'),

]