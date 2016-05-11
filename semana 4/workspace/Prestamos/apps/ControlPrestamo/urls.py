from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', principal, name='main'),
    url(r'^Estudiantes/', alumnos, name='listaE'),
    url(r'^Articulos/', articulos , name='listaA'),
    url(r'^Prestamos/$', prestamos, name='listaP'),
    url(r'^login/', login, name="login"),
]
