from django.contrib import admin

# Register your models here.
from aerolinea.models import Asiento, Avion, Boleto, Pasajero, Reserva, Vuelo

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'capacidad', 'filas', 'columnas')
    list_filter = ('modelo',)
    search_fields = ('modelo', 'capacidad')


@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'fecha_salida', 'fecha_llegada', 'duracion', 'estado', 'precio_base')
    search_fields = ('destino',)


@admin.register(Asiento)
class AsientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'avion_id', 'numero', 'fila', 'columna', 'tipo', 'estado')
    list_filter = ('avion_id',)
    search_fields = ('avion_id', 'numero')

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'documento', 'email', 'telefono', 'fecha_nacimiento', 'tipo_documento')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'documento')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vuelo_id', 'pasajero_id', 'asiento_id', 'estado', 'fecha_reserva', 'precio', 'codigo_reserva')
    list_filter = ('vuelo_id', 'pasajero_id', 'fecha_reserva')
    search_fields = ('vuelo_id', 'pasajero_id')

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva_id', 'codigo_barra', 'fecha_emision', 'estado')
    list_filter = ('reserva_id',)
    search_fields = ('reserva_id', 'fecha_emision')
