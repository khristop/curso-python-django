from django.conf.urls import url
from .views import principal #Principal
urlpatterns = [
    #url(r'^$', Principal.as_view()),
    url(r'^$', principal),
]
