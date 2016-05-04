from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.template.context_processors import request

# Create your views here.
#class Principal(View):
#    template_name = 'index'

def principal(request):
    diccionario= {'Carlos':'10','Alcide':'5',}
    return render_to_response('index.html',{
                                            'variable':'Christopher',
                                            'lista':diccionario})