from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms
import datetime
from django.contrib.auth import authenticate, login
from django.db.models import Q

from .models import GestionReservaMedica

from django.views.generic import View, DeleteView, UpdateView, FormView, ListView

#SECCION RESERVAS
from .models import GestionReservaMedica
from .forms import ReservaMedicaCreateForm
from .forms import ReservaMedicaUpdateForm

#SECCION FUNCIONARIO
from .models import GestionFuncionario
from .forms import FuncionarioCreateForm
from .forms import FuncionarioUpdateForm

#SECCION INVENTARIO
from .models import GestionInventario
from .forms import InventarioCreateForm
from .forms import InventarioUpdateForm

#LOGIN

from .forms import LoginForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, 'home.html', context)

#SECCION RESERVAS MEDICAS

class GestionReservasView(View):
    def get(self, request, *args, **kwargs):
        reservasmedicas=GestionReservaMedica.objects.all()
        context={'reservasmedicas' : reservasmedicas}
        return render(request, 'gestionreservas.html', context)


class ReservaMedicaCreateView(View):
    def get(self, request,*args, **kwargs):
        form = ReservaMedicaCreateForm()
        context = {'form': form}
        return render(request,'reservamedicacreate.html', context)

    def post(self, request):
        form = ReservaMedicaCreateForm(request.POST)
        fechaReserva = request.POST.get('fechaReserva')
        fechaReservaDate = datetime.datetime.strptime(fechaReserva, '%Y-%m-%d')
        horaReserva = request.POST.get('horaReserva')
        nombreCliente = request.POST.get('nombreCliente')
        apellidoCliente = request.POST.get('apellidoCliente')
        telefonoCliente = request.POST.get('telefonoCliente')        
        now = datetime.datetime.now()
        if not telefonoCliente.isdigit():
            messages.error(request, 'El telefono solo debe contener numeros')
            return render(request, 'reservamedicacreate.html', {'form': form}) 
        if not nombreCliente.isalpha():
            messages.error(request, 'El nombre solo puede contener letras')
            return render(request, 'reservamedicacreate.html', {'form': form})
        if not apellidoCliente.isalpha():
            messages.error(request, 'El apellido solo puede contener letras')
            return render(request, 'reservamedicacreate.html', {'form': form})
        if fechaReservaDate < now:
            messages.error(request, 'La fecha de la reserva no puede ser en el pasado.')
            return render(request, 'reservamedicacreate.html', {'form': form})
        if GestionReservaMedica.objects.filter(fechaReserva=fechaReserva).exists() and GestionReservaMedica.objects.filter(horaReserva=horaReserva).exists():
            messages.error(request, 'No pueden haber dos reservas el mismo día a la misma hora.')
            return render(request, 'reservamedicacreate.html', {'form': form})
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva creada satisfactoriamente.')
            return redirect('gestionreservas')
        context = {"form":form}
        return render(request, "gestionreservas.html", context)

class ReservaMedicaUpdateView(UpdateView):
    model = GestionReservaMedica
    form_class = ReservaMedicaUpdateForm
    template_name= 'reservamedicaupdate.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('gestionreservas')

class ReservaMedicaDeleteView(DeleteView):
    model = GestionReservaMedica
    template_name = 'reservamedicadelete.html'
    success_url = reverse_lazy('gestionreservas')

#TERMINO SECCION RESERVAS




# SECCION FUNCIONARIOS

class GestionFuncionariosView(View):
    def get(self, request, *args, **kwargs):
        gestionfuncionarios=GestionFuncionario.objects.all()
        context={'gestionfuncionarios' : gestionfuncionarios}
        return render(request, 'gestionfuncionarios.html', context)

class FuncionarioCreateView(View):
    def get(self, request,*args, **kwargs):
        form = FuncionarioCreateForm()
        context = {'form': form}
        return render(request,'funcionariocreate.html', context)

    def post(self, request):
        form = FuncionarioCreateForm(request.POST)
        nombreFuncionario = request.POST.get('nombreFuncionario')
        telefonoFuncionario = request.POST.get('telefonoFuncionario')
        telefonoEmergencia = request.POST.get('telefonoEmergencia')
        if not telefonoEmergencia.isdigit():
            messages.error(request, 'El telefono de emergencia solo puede contener numeros')
            return render(request, 'funcionariocreate.html', {'form':form})
        if not telefonoFuncionario.isdigit():
            messages.error(request, 'El telefono solo puede contener numeros')
            return render(request, 'funcionariocreate.html', {'form':form})
        if not nombreFuncionario.isalpha():
            messages.error(request, 'El nombre solo puede contener letras')
            return render(request, 'funcionariocreate.html', {'form':form})
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionario añadido correctamente.')
            return redirect('gestionfuncionarios')
        context = {"form":form}
        return render(request, "gestionfuncionarios.html", context)

class FuncionarioUpdateView(UpdateView):
    model = GestionFuncionario
    form_class = FuncionarioUpdateForm
    template_name= 'funcionarioupdate.html'


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('gestionfuncionarios')

class FuncionarioDeleteView(DeleteView):
    model = GestionFuncionario
    template_name = 'funcionariodelete.html'
    success_url = reverse_lazy('gestionfuncionarios')

#TERMINO SECCION FUNCIONARIOS

        


# SECCION INVENTARIO

class GestionInventarioView(View):
    def get(self, request, *args, **kwargs):
        gestioninventarios=GestionInventario.objects.all()
        context={'gestioninventarios' : gestioninventarios}
        return render(request, 'gestioninventarios.html', context)

class InventarioCreateView(View):
    def get(self, request,*args, **kwargs):
        form = InventarioCreateForm()
        context = {'form': form}
        return render(request,'inventariocreate.html', context)

    def post(self, request):
        form = InventarioCreateForm(request.POST)
        nombreProducto = request.POST.get('nombreProducto')
        telefonoProveedor = request.POST.get('telefonoProveedor')
        if not telefonoProveedor.isdigit():
            messages.error(request, 'El telefono solo puede contener numeros')
            return render(request, 'funcionariocreate.html', {'form':form})
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido correctamente.')
            return redirect('gestioninventarios')
        context = {"form":form}
        return render(request, "gestioninventarios.html", context)

class InventarioUpdateView(UpdateView):
    model = GestionInventario
    form_class = InventarioUpdateForm
    template_name= 'inventarioupdate.html'


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('gestioninventarios')

class InventarioDeleteView(DeleteView):
    model = GestionInventario
    template_name = 'inventariodelete.html'
    success_url = reverse_lazy('gestioninventarios')


#TERMINO SECCION INVENTARIO


# SECCION LOGIN
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = 'success_url'
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('home')
        return super().form_valid(form)

#SEARCH 
class SearchView(ListView):
    model = GestionReservaMedica
    template_name = 'search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query and self.model.objects.filter(rutCliente__contains=query):
            return self.model.objects.filter(rutCliente__contains=query)
        if query and self.model.objects.filter(nombreCliente__contains=query):
            return self.model.objects.filter(nombreCliente__contains=query)
        return self.model.objects.all()

class SearchViewFuncionarios(ListView):
    model = GestionFuncionario
    template_name = 'search_resultsfuncionarios.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query and self.model.objects.filter(nombreFuncionario__contains=query):
            return self.model.objects.filter(nombreFuncionario__contains=query)
        if query and self.model.objects.filter(rutFuncionario__contains=query):
            return self.model.objects.filter(rutFuncionario__contains=query)
        return self.model.objects.all()

class SearchViewInventario(ListView):
    model = GestionInventario
    template_name = 'search_resultsinventario.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query and self.model.objects.filter(nombreProducto__contains=query):
            return self.model.objects.filter(nombreProducto__contains=query)
        if query and self.model.objects.filter(nombreProveedor__contains=query):
            return self.model.objects.filter(nombreProveedor__contains=query)
        return self.model.objects.all()

