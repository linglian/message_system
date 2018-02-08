from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^send/$', views.send, name='send'),
    url(r'^get/$', views.get, name='send'),
    url(r'^index/$', views.index, name='index'),
    path('', views.index, name='index'),
]