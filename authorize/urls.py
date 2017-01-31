from django.conf.urls import url
from .views import index, authorized, login, logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^authorized/$', authorized, name='authorized'),
]