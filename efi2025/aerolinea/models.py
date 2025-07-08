from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Avion(models.Model):
    modelo = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    filas = models.IntegerField()
    columnas = models.IntegerField()

    def __str__(self):
        return f"Modelo {self.modelo} - Capacidad {self.capacidad}"


class Vuelo(models.Model):
    avion_id = models.ForeignKey(
        Avion,
        on_delete=models.CASCADE
    )
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.IntegerField()
    estado = models.CharField(
        max_length=12,
        choices=[
            ('programado', _('Programado')),
            ('en_vuelo', _('En vuelo')),
            ('completado', _('Completado')),
            ('cancelado', _('Cancelado')),
        ],
    )
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.destino


class Pasajero(models.Model):
    nombre = models.CharField(max_length=256)
    documento = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()
    tipo_documento = models.CharField(max_length=25, 
        choices= [
            ('DNI', 'DNI'),
            ('Pasaporte', _('Pasaporte')),
            ('Cedula', _('Cédula')),            
        ])
    
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre


class Asiento(models.Model):
    avion_id = models.ForeignKey(
        Avion,
        on_delete=models.CASCADE
    )
    numero = models.IntegerField()
    fila = models.CharField(max_length=25)
    columna = models.CharField(max_length=25)
    tipo = models.CharField(
        max_length=12,
        choices=[
            ('economico', _('Económico')),
            ('premium', 'Premium'),
            ('ejecutivo', _('Ejecutivo')), 
        ],
    )
    estado = models.CharField(
        max_length=12,
        choices=[
            ('disponible', _('Disponible')),
            ('reservado', _('Reservado')),
            ('ocupado', _('Ocupado')),            
        ],
    )

    def __str__(self):
        return f"Asiento {self.numero} - {self.estado}"


    
class Reserva(models.Model):
    vuelo_id = models.ForeignKey(
        Vuelo,
        on_delete=models.CASCADE,
        related_name='reservas_vuelo'
    )
    pasajero_id = models.ForeignKey(
        Pasajero,
        on_delete=models.CASCADE
    ) 
    asiento_id = models.ForeignKey(
            Asiento,
            on_delete=models.CASCADE,
            related_name='reservas_asiento',
    )
    estado = models.CharField(
            max_length=12,
            choices=[
                ('pendiente', _('Pendiente')),
                ('confirmada', _('Confirmada')),
                ('cancelada', _('Cancelada')),
            ],
        )
    fecha_reserva = models.DateTimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_reserva = models.CharField(max_length=50, unique=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - Pasajero {self.pasajero_id.nombre}"

    class Meta:
        unique_together = [
            ('vuelo_id', 'asiento_id'),
            ('vuelo_id', 'pasajero_id'),
        ]


class Usuario(models.Model):
   username = models.CharField(max_length=150)
   password = models.CharField(max_length=30)
   email = models.EmailField()
   rol = models.CharField(
        max_length=12,
        choices=[
            ('staff', 'Staff'),
            ('pasajero', _('Pasajero'))
        ],
    )

   def __str__(self):
        return self.username

   
class Boleto(models.Model):
    reserva_id = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=30, unique=True)
    fecha_emision = models.DateTimeField()
    estado = models.CharField(
        max_length=25,
        choices=[
            ('emitido', _('Emitido')),
            ('cancelado', _('Cancelado')),
            ('abordado', _('Abordado')),
            ('check-in realizado', _('Check-in Realizado'))
        ],
    )

    def __str__(self):
        return f"Boleto para {self.reserva_id.pasajero_id.nombre} - Código {self.codigo_barra}"
