from django.views.generic.list import ListView
from applications import departamento
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.


class NewDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '.'

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shortname=form.cleaned_data['shorname']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        print('Esta en el form-.--------')
        return super(NewDepartamento, self).form_valid(form)


class DepartarmentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'
