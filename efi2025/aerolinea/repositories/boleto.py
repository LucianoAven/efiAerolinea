from typing import Optional
from aerolinea.models import Boleto, Reserva


class BoletoRepository:
    """
    Clase que se conecta con la base de datos para manejar boletos
    """
    @staticmethod
    def create(
        reserva_id: Reserva,
        codigo_barra: str,
        fecha_emision: str,
        estado: str
    ) -> Boleto:
        """
        Crear un nuevo boleto.
        """
        return Boleto.objects.create(
            reserva_id=reserva_id,
            codigo_barra=codigo_barra,
            fecha_emision=fecha_emision,
            estado=estado
        )


    @staticmethod
    def delete(boleto_id) -> bool:
        """
        Eliminar un boleto.
        """
        try:
            Boleto.objects.get(id=boleto_id).delete()
        except Boleto.DoesNotExist:
            raise ValueError("No se encontró el boleto")


    @staticmethod
    def update(
        boleto: Boleto,
        reserva_id: Reserva = None,
        codigo_barra: str = None,
        fecha_emision: str = None,
        estado: str = None
    ) -> Boleto:
        """
        Actualizar un boleto
        """
        if reserva_id is not None:
            boleto.reserva_id = reserva_id
        if codigo_barra is not None:
            boleto.codigo_barra = codigo_barra
        if fecha_emision is not None:
            boleto.fecha_emision = fecha_emision
        if estado is not None:
            boleto.estado = estado
            
        boleto.save()
        return boleto


    @staticmethod
    def get_all() -> list[Boleto]:
        """
        Obtener todos los boletos.
        """
        return Boleto.objects.all()


    @staticmethod
    def get_by_id(boleto_id: int) -> Optional[Boleto]:
        """
        Obtener un boleto mediante su id.
        """
        try:
            return Boleto.objects.get(id=boleto_id)
        except Boleto.DoesNotExist:
            return None    


    @staticmethod
    def get_by_codigo(codigo_barra: str) -> Optional[Boleto]:
        """
        Obtener boleto por código de barras.
        """
        try:
            return Boleto.objects.get(codigo_barra=codigo_barra)
        except Boleto.DoesNotExist:
            return None


    @staticmethod
    def get_by_reserva(reserva_id: int) -> list[Boleto]:
        """
        Obtener boletos por reserva.
        """
        return Boleto.objects.filter(reserva_id=reserva_id)


    @staticmethod
    def get_by_estado(estado: str) -> list[Boleto]:
        """
        Obtener boletos por estado.
        """
        return Boleto.objects.filter(estado=estado)