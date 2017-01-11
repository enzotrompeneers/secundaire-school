from django.conf.urls import url
from CRUD import views

urlpatterns = [
   
    url(r'^[iI]ndex/$', views.home, name='home'),
    url(r'^[hH]ome/$', views.home, name='home'),
    url(r'^[aA]anbod/$', views.aanbod, name='aanbod'),
    url(r'^[oO]ns[/s] [aA]anbod/$', views.aanbod, name='aanbod'),
    url(r'^[wW]ie/$', views.wie, name='wie'),
    url(r'^[cC]ontact/$', views.contact, name='contact'),
    
    url(r'^[rR]ichtingen/$', views.richtingen, name='richtingen'),
    url(r'^[lL]eraren/$', views.leraren, name='leraren'),
    url(r'^[kK]lassen/$', views.klassen, name='klassen'),

     url(r'^', views.home, name='home'), #must be last else always home because regex is always found
]