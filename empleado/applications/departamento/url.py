
from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"


def desdeDepartamento():
    print('$$$$$$$$$$$$$$$$$$$departamento$$$$$$$$$$$$$$$$$$$$$$')


urlpatterns = [
    path('new-departamento/', views.NewDepartamento.as_view(),
         name='nuevo_departamento'),
    path(
        'departamento-lista/',
        views.DepartarmentoListView.as_view(),
        name='departamento_list'
    )




]
