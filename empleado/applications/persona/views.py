from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
)


# Models
from .models import Empleado
from .forms import EmpleadoForm 
# Create your views here.


class EmpleadoListView(ListView):
    template_name = 'persona/list_all.html'
    paginate_by=4
    ordering='first_name'
    
    def get_queryset(self):
        
        # Recupero la palabra en donde el id sea kword
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

    # Lista de empleados por area


class EmpleadoAdminListView(ListView):
    template_name = 'persona/lista_empleados.html'
    model=Empleado
    paginate_by=10
    ordering='first_name'
    context_object_name='empleado'
    

class ByAreaEmpleadoListView(ListView):
    template_name = 'persona/list_area_all.html'
    context_object_name='empleados'
    def get_queryset(self):
        area = self.kwargs['nombre']
        lista = Empleado.objects.filter(
            departamento__shortname=area
        )
        return lista


class ByTrabajoListView(ListView):
    template_name = 'persona/list_trabajo.html'

    def get_queryset(self):
        trabajo1 = self.kwargs['trabajo']
        lista = Empleado.objects.filter(
            job=trabajo1
        )
        return lista


class ListEmpleadosByKwords(ListView):
    template_name = 'persona/by-kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        # Recupero la palabra en donde el id sea kword
        palabra_clave = self.request.GET.get('kword',)
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )

        return lista


class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/ability-list.html'
    context_object_name = 'abilities'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)

        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle-empleado.html"


class SuccesView(TemplateView):
    template_name = "persona/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/crear.html"
    form_class=EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # almacena todo lo recuperado del form en la base de datos.
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class UpdateUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # almacena todo lo recuperado del form en la base de datos.

        return super(UpdateUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


class InicioView(TemplateView):

    template_name = 'inicio.html'
