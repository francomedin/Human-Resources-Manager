from applications.home.models import Prueba
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Vistas basadas en clases


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['1', '2', '3', '4']


class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = 'home/crear.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '.'
