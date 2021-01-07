
from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-todo-empleado/',
        views.EmpleadoListView.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-area-empleado/<nombre>',
        views.ByAreaEmpleadoListView.as_view(),
        name='empleados-por-area'
    ),
    path('lista-empleados-admin/',
         views.EmpleadoAdminListView.as_view(),
         name='empleados_admin'

         ),
    path('listar-trabajo-empleado/<trabajo>',
         views.ByTrabajoListView.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKwords.as_view()),
    path('listar-habilidades-empleado/',
         views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path('crear-empleado/',
         views.EmpleadoCreateView.as_view(),
         name='crear-empleado'
         ),
    path(
        'succes/',
        views.SuccesView.as_view(),
        name='correcto'
    ),
    path('update-empleado/<pk>', views.UpdateUpdateView.as_view(),
         name='modificar_empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(),
         name='eliminar_empleado'),




]
