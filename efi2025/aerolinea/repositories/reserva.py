from typing import Optional
from aerolinea.models import Reserva, Vuelo, Pasajero, Asiento

class ReservaRepository:
    """
    Clase que se conecta con la base de datos para manejar reservas
    """
    @staticmethod
    def create(
        vuelo_id: Vuelo,
        pasajero_id: Pasajero,
        asiento_id: Asiento,
        estado: str,
        fecha_reserva: str,
        precio: float,
        codigo_reserva: str
    ) -> Reserva:
        """
        Crear una nueva reserva.
        """
        return Reserva.objects.create(
            vuelo_id=vuelo_id,
            pasajero_id=pasajero_id,
            asiento_id=asiento_id,
            estado=estado,
            fecha_reserva=fecha_reserva,
            precio=precio,
            codigo_reserva=codigo_reserva
        )
    
    @staticmethod
    def delete(reserva: Reserva) -> bool:
        """
        Eliminar una reserva.
        """
        try:
            reserva.delete()
            return True
        except Reserva.DoesNotExist:
            raise ValueError("No se encontró la reserva")

    @staticmethod
    def update(
        reserva: Reserva,
        vuelo_id: Vuelo = None,
        pasajero_id: Pasajero = None,
        asiento_id: Asiento = None,
        estado: str = None,
        fecha_reserva: str = None,
        precio: float = None,
        codigo_reserva: str = None
    ) -> Reserva:
        """
        Actualizar una reserva
        """
        if vuelo_id is not None:
            reserva.vuelo_id = vuelo_id
        if pasajero_id is not None:
            reserva.pasajero_id = pasajero_id
        if asiento_id is not None:
            reserva.asiento_id = asiento_id
        if estado is not None:
            reserva.estado = estado
        if fecha_reserva is not None:
            reserva.fecha_reserva = fecha_reserva
        if precio is not None:
            reserva.precio = precio
        if codigo_reserva is not None:
            reserva.codigo_reserva = codigo_reserva
            
        reserva.save()
        return reserva

    @staticmethod
    def get_all() -> list[Reserva]:
        """
        Obtener todas las reservas.
        """
        return Reserva.objects.all()
    
    @staticmethod
    def get_by_id(reserva_id: int) -> Optional[Reserva]:
        """
        Obtener una reserva mediante su id.
        """
        try:
            return Reserva.objects.get(id=reserva_id)
        except Reserva.DoesNotExist:
            return None    

    @staticmethod
    def get_by_codigo(codigo_reserva: str) -> Optional[Reserva]:
        """
        Obtener reserva por código.
        """
        try:
            return Reserva.objects.get(codigo_reserva=codigo_reserva)
        except Reserva.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_pasajero(pasajero_id: int) -> list[Reserva]:
        """
        Obtener reservas por pasajero.
        """
        return Reserva.objects.filter(pasajero_id=pasajero_id)
    
    @staticmethod
    def get_by_vuelo(vuelo_id: int) -> list[Reserva]:
        """
        Obtener reservas por vuelo.
        """
        return Reserva.objects.filter(vuelo_id=vuelo_id)
    
    @staticmethod
    def get_by_estado(estado: str) -> list[Reserva]:
        """
        Obtener reservas por estado.
        """
        return Reserva.objects.filter(estado=estado)