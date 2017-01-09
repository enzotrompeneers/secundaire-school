from django.conf.urls import url
from CRUD import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^[iI]ndex/$', views.home, name='home'),
    url(r'^[hH]ome/$', views.home, name='home'),
    url(r'^[aA]anbod/$', views.aanbod, name='aanbod'),
    url(r'^[oO]ns[/s] [aA]anbod/$', views.aanbod, name='aanbod'),
    url(r'^[wW]ie/$', views.wie, name='wie'),
    url(r'^[cC]ontact/$', views.contact, name='contact'),

    url(r'^create/$', views.create, name='create'),
    url(r'^read/$', views.read, name='read'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
]