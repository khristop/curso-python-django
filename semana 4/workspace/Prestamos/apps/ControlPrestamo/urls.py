from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', principal, name='main'),
    url(r'^Estudiantes/', alumnos, name='listaE'),
]
