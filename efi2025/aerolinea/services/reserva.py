
from typing import Optional
from aerolinea.models import Reserva, Vuelo, Pasajero, Asiento
from .reserva import ReservaRepository


class ReservaService:

    @staticmethod
    def crear_reserva(vuelo_id: Vuelo, pasajero_id: Pasajero, asiento_id: Asiento, estado: str, fecha_reserva: str, precio: float, codigo_reserva: str) -> Reserva:
        return ReservaRepository.create(vuelo_id, pasajero_id, asiento_id, estado, fecha_reserva, precio, codigo_reserva)

    @staticmethod
    def eliminar_reserva(reserva_id: int) -> bool:
        reserva = ReservaRepository.get_by_id(reserva_id)
        if not reserva:
            raise ValueError("Reserva no encontrada")
        return ReservaRepository.delete(reserva)

    @staticmethod
    def actualizar_reserva(
        reserva_id: int,
        vuelo_id: Optional[Vuelo] = None,
        pasajero_id: Optional[Pasajero] = None,
        asiento_id: Optional[Asiento] = None,
        estado: Optional[str] = None,
        fecha_reserva: Optional[str] = None,
        precio: Optional[float] = None,
        codigo_reserva: Optional[str] = None
    ) -> Reserva:
        reserva = ReservaRepository.get_by_id(reserva_id)
        if not reserva:
            raise ValueError("Reserva no encontrada")
        return ReservaRepository.update(
            reserva=reserva,
            vuelo_id=vuelo_id,
            pasajero_id=pasajero_id,
            asiento_id=asiento_id,
            estado=estado,
            fecha_reserva=fecha_reserva,
            precio=precio,
            codigo_reserva=codigo_reserva
        )


    @staticmethod
    def obtener_reserva(reserva_id: int) -> Optional[Reserva]:
        return ReservaRepository.get_by_id(reserva_id)

    @staticmethod
    def listar_reservas() -> list[Reserva]:
        return ReservaRepository.get_all()

    @staticmethod
    def buscar_por_codigo(codigo_reserva: str) -> Optional[Reserva]:
        return ReservaRepository.get_by_codigo(codigo_reserva)

    @staticmethod
    def obtener_por_pasajero(pasajero_id: int) -> list[Reserva]:
        return ReservaRepository.get_by_pasajero(pasajero_id)

    @staticmethod
    def obtener_por_vuelo(vuelo_id: int) -> list[Reserva]:
        return ReservaRepository.get_by_vuelo(vuelo_id)

    @staticmethod
    def obtener_por_estado(estado: str) -> list[Reserva]:
        return ReservaRepository.get_by_estado(estado)
