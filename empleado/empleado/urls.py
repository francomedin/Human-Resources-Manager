
from applications import home
from django.contrib import admin
from django.urls import path, re_path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos las url de la carpeta applications
    re_path('',include('applications.departamento.url')),
    re_path('',include('applications.home.url')),
    re_path('',include('applications.persona.url')),
    
    
  
    
]
