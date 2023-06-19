from django.contrib import admin
from .models import GestionReservaMedica
# Register your models here.

class ReservaMedicaAdmin(admin.ModelAdmin):
    list_display = ['nombreCliente','apellidoCliente','rutCliente', 'telefonoCliente','direccionCliente', 'fechaReserva', 'horaReserva', 'mascotaCliente']

admin.site.register(GestionReservaMedica, ReservaMedicaAdmin)