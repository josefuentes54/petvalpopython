"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from petvalpo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),

    path('gestionreservas/', views.GestionReservasView.as_view(), name='gestionreservas'),
    path('reservamedicacreate/', views.ReservaMedicaCreateView.as_view(), name='reservamedicacreate'),
    path('<int:pk>/reservamedicaupdate/', views.ReservaMedicaUpdateView.as_view(), name='reservamedicaupdate'),
    path('<int:pk>/reservamedicadelete/', views.ReservaMedicaDeleteView.as_view(), name='reservamedicadelete'),
    
    
    path('gestionfuncionarios/', views.GestionFuncionariosView.as_view(), name='gestionfuncionarios'),
    path('funcionariocreate/', views.FuncionarioCreateView.as_view(), name='funcionariocreate'),
    path('<int:pk>/funcionarioupdate/', views.FuncionarioUpdateView.as_view(), name='funcionarioupdate'),
    path('<int:pk>/funcionariodelete/', views.FuncionarioDeleteView.as_view(), name='funcionariodelete'),


    path('gestioninventarios/', views.GestionInventarioView.as_view(), name='gestioninventarios'),
    path('inventariocreate/', views.InventarioCreateView.as_view(), name='inventariocreate'),
    path('<int:pk>/inventarioupdate/', views.InventarioUpdateView.as_view(), name='inventarioupdate'),
    path('<int:pk>/inventariodelete/', views.InventarioDeleteView.as_view(), name='inventariodelete'),

    path('search/',views.SearchView.as_view(), name='search'),
    path('searchfuncionarios/',views.SearchViewFuncionarios.as_view(), name='searchfuncionario'),
    path('searchinventario/',views.SearchViewInventario.as_view(), name='searchinventario'),
    
    
 
]
