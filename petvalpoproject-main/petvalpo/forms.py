from django import forms
import datetime
from .models import GestionReservaMedica
from .models import GestionFuncionario
from .models import GestionInventario
from django.contrib.auth.forms import AuthenticationForm




class DateInput(forms.DateInput):
    input_type = 'date'

#FORMULARIO RESERVA MEDICA
class ReservaMedicaCreateForm(forms.ModelForm):

    fechaReserva = forms.DateField(widget=DateInput)
    horaReserva = forms.TimeField(required=True)
    class Meta:
        model = GestionReservaMedica
        fields = ['nombreCliente', 'apellidoCliente', 'rutCliente','telefonoCliente','direccionCliente','fechaReserva','horaReserva','mascotaCliente']
        labels = {
            'nombreCliente': 'Nombre de cliente',
            'apellidoCliente': 'Apellido de cliente',
            'rutCliente': 'Rut',
            'telefonoCliente': 'Telefono',
            'direccionCliente': 'Direccion',
            'fechaReserva': 'Fecha reserva',
            'horaReserva': 'Hora reserva',
            'mascotaCliente': 'Nombre Mascota'
        }

class ReservaMedicaUpdateForm(forms.ModelForm):
    fechaReserva = forms.DateField(widget=DateInput, label= 'Fecha de reserva')

    class Meta:
        model = GestionReservaMedica
        fields = ('nombreCliente', 'apellidoCliente', 'rutCliente', 'telefonoCliente','direccionCliente','fechaReserva', 'horaReserva', 'mascotaCliente')
        labels = {
            'nombreCliente': 'Nombre de cliente',
            'apellidoCliente': 'Apellido de cliente',
            'rutCliente': 'Rut',
            'telefonoCliente': 'Telefono',
            'direccionCliente': 'Direccion',
            'fechaReserva': 'Fecha reserva',
            'horaReserva': 'Hora de reserva',
            'mascotaCliente': 'Nombre de mascota'
        }
        
    def clean(self):
        cleaned_data = super().clean()
        nombreCliente = cleaned_data.get('nombreCliente')
        apellidoCliente = cleaned_data.get('apellidoCliente')
        fechaReserva = cleaned_data.get('fechaReserva')
        horaReserva = cleaned_data.get('horaReserva')
        now = datetime.datetime.now().date()
        if fechaReserva < now:
            raise forms.ValidationError('La fecha de la reserva no puede ser en el pasado.')
        if GestionReservaMedica.objects.filter(fechaReserva=fechaReserva).exists() and GestionReservaMedica.objects.filter(horaReserva=horaReserva).exists():
            raise forms.ValidationError('No pueden haber dos reservas el mismo día a la misma hora.')
        if not apellidoCliente.isalpha():
            raise forms.ValidationError('El apellido solo puede contener letras')
        if not nombreCliente.isalpha():
            raise forms.ValidationError('El nombre solo puede contener letras')
        return cleaned_data

#TERMINO FORMULARIO RESERVA MEDICA
#FORMULARIO  FUNCIONARIO
class FuncionarioCreateForm(forms.ModelForm):

    class Meta:
        model = GestionFuncionario
        fields = ['nombreFuncionario', 'apellidoFuncionario', 'rutFuncionario','telefonoFuncionario','direccionFuncionario','contactoEmergencia','telefonoEmergencia']
        labels = {
            'nombreFuncionario': 'Nombre de Funcionario',
            'apellidoFuncionario': 'Apellido de Funcionario',
            'rutFuncionario': 'Rut',
            'telefonoFuncionario': 'Telefono',
            'direccionFuncionario': 'Direccion',
            'contactoEmergencia': 'Contacto Emergencia',
            'telefonoEmergencia': 'Telefono Emergencia',
            
        }
class FuncionarioUpdateForm(forms.ModelForm):
      
    class Meta:
        model = GestionFuncionario
        fields = ('nombreFuncionario', 'apellidoFuncionario', 'rutFuncionario','telefonoFuncionario','direccionFuncionario','contactoEmergencia','telefonoEmergencia')
        labels = {
            'nombreFuncionario': 'Nombre de Funcionario',
            'apellidoFuncionario': 'Apellido de Funcionario',
            'rutFuncionario': 'Rut',
            'telefonoFuncionario': 'Telefono',
            'direccionFuncionario': 'Direccion',
            'contactoEmergencia': 'Contacto Emergencia',
            'telefonoEmergencia': 'Telefono Emergencia',
            
        }
    def clean(self):
        cleaned_data = super().clean()
        nombreFuncionario = cleaned_data.get('nombreFuncionario')
        apellidoFuncionario = cleaned_data.get('apellidoFuncionario')
        telefonoFuncionario = cleaned_data.get('telefonoFuncionario')
        telefonoEmergencia = cleaned_data.get('telefonoEmergencia')
        if not apellidoFuncionario.isalpha():
            raise forms.ValidationError('El apellido solo puede contener letras')
        if not nombreFuncionario.isalpha():
            raise forms.ValidationError('El nombre solo puede contener letras')
        if not telefonoFuncionario.isdigit():
            raise forms.ValidationError('El telefono solo debe contener numeros')
        if not telefonoEmergencia.isdigit():
            raise forms.ValidationError('El telefono de emergencia solo debe contener numeros')
        return cleaned_data
        

#TERMINO FORMULARIO FUNCIONARIO

class InventarioCreateForm(forms.ModelForm):
    
    fechaCompra = forms.DateField(widget=DateInput, label='Fecha de compra')
    class Meta:
        model = GestionInventario
        fields = ['nombreProducto', 'cantidadProducto', 'fechaCompra', 'nombreProveedor', 'telefonoProveedor']
        labels = {
            'nombreProducto': 'Nombre del Producto',
            'cantidadProducto': 'Cantidad de Producto',
            'fechaCompra': 'Fecha Compra',
            'nombreProveedor': 'Nombre de Proveedor',
            'telefonoProveedor': 'Telefono de Proveedor',
        }

class InventarioUpdateForm(forms.ModelForm):
    
    fechaCompra = forms.DateField(widget=DateInput, label='Fecha de compra')
    class Meta:
        model = GestionInventario
        fields = ('nombreProducto', 'cantidadProducto', 'fechaCompra', 'nombreProveedor', 'telefonoProveedor')
        labels = {
            'nombreProducto': 'Nombre del Producto',
            'cantidadProducto': 'Cantidad de Producto',
            'fechaCompra': 'Fecha Compra',
            'nombreProveedor': 'Nombre Proveedor',
            'telefonoProveedor': 'Telefono Proveedor',
                       
        }
    def clean(self):
        cleaned_data = super().clean()
        nombreProducto = cleaned_data.get('nombreProducto')
        cantidadProducto = cleaned_data.get('cantidadProdcuto')
        fechaCompra = cleaned_data.get('fechaCompra')
        nombreProveedor = cleaned_data.get('nombreProveedor')
        telefonoProveedor = cleaned_data.get('telefonoProveedor')
        if not nombreProveedor.isalpha():
            raise forms.ValidationError('El nombre del proveedor solo puede contener letras')
        return cleaned_data

# AUTENTICACIÓN

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Usuario y/o contraseña incorrectos.'
    }
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

