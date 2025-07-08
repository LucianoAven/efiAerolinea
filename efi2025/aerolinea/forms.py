
from django import forms
from aerolinea.models import Asiento, Avion, Boleto, Pasajero, Reserva, Vuelo


class AvionForm(forms.ModelForm):

    # Formulario de creacion de aviones

    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']
        widgets = {
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control w-25 personalizado',
                    'placeholder': 'Ingrese el nombre del modelo',
                    'style': 'background: aquamarine'
                }
            )
        }


class VueloForm(forms.ModelForm):

    # Formulario de creacion de vuelos

    class Meta:
        model = Vuelo
        fields = ['avion_id', 'origen', 'destino', 'fecha_salida', 'fecha_llegada', 'duracion', 'estado', 'precio_base']
        widgets = {
            'avion_id': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha_salida': forms.DateTimeInput(
                attrs={'class': 'form-control w-50', 'type': 'datetime-local'}
            ),
            'fecha_llegada': forms.DateInput(
                attrs={'class': 'form-control w-50', 'type': 'datetime-local'}
            ),
            'duracion': forms.NumberInput(
                attrs={'class': 'form-control w-25'}
            ),            

        }


class PasajeroForm(forms.ModelForm):

    # Formulario de creacion de pasajeros

    class Meta:
        model = Pasajero
        fields = ['nombre', 'documento', 'email', 'telefono', 'fecha_nacimiento', 'tipo_documento']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': 'Ingrese el nombre del pasajero'
                }
            ),
            'documento': forms.TextInput(
                attrs={'class': 'form-control w-50'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control w-50'}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'form-control w-50'}
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control w-50', 'type': 'date'}
            ),
            'tipo_documento': forms.Select(
                attrs={'class': 'form-control w-50'}
            ),
        }


class ReservaForm(forms.ModelForm):

    # Formulario de creacion de reservas

    class Meta:
        model = Reserva
        fields = ['vuelo_id', 'pasajero_id', 'asiento_id', 'estado', 'fecha_reserva', 'precio', 'codigo_reserva']
        widgets = {
           'avion_id': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha_reserva': forms.DateInput(
                attrs={'class': 'form-control w-50', 'type': 'date'}
            ),
        }


class AsientoForm(forms.ModelForm):

    # Formulario de creacion de asientos

    class Meta:
        model = Asiento
        fields = ['avion_id', 'numero', 'fila', 'columna', 'tipo', 'estado']
        widgets = {
            'avion_id': forms.Select(
                attrs={'class': 'form-control'}
            ),
            
        }


class BoletoForm(forms.ModelForm):

    # Formulario de creacion de boletos

    class Meta:
        model = Boleto
        fields = ['reserva_id', 'codigo_barra', 'fecha_emision', 'estado']
        widgets = {
            'reserva_id': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'codigo_barra': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': 'Ingrese el codigo'
                }
            ),
            'fecha_emision': forms.DateInput(
                attrs={'class': 'form-control w-50', 'type': 'date'}
            ),            
            'estado': forms.Select(
                attrs={'class': 'form-control w-50'}
            ),
        }
