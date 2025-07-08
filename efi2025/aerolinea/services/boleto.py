
from typing import Optional
from aerolinea.models import Boleto, Reserva
from .boleto import BoletoRepository


class BoletoService:

    @staticmethod
    def crear_boleto(reserva_id: Reserva, codigo_barra: str, fecha_emision: str, estado: str) -> Boleto:
        return BoletoRepository.create(reserva_id, codigo_barra, fecha_emision, estado)

    @staticmethod
    def eliminar_boleto(boleto_id: int) -> bool:
        boleto = BoletoRepository.get_by_id(boleto_id)
        if not boleto:
            raise ValueError("Boleto no encontrado")
        return BoletoRepository.delete(boleto_id)

    @staticmethod
    def actualizar_boleto(
        boleto_id: int,
        reserva_id: Optional[Reserva] = None,
        codigo_barra: Optional[str] = None,
        fecha_emision: Optional[str] = None,
        estado: Optional[str] = None
    ) -> Boleto:
        boleto = BoletoRepository.get_by_id(boleto_id)
        if not boleto:
            raise ValueError("Boleto no encontrado")
        return BoletoRepository.update(
            boleto=boleto,
            reserva_id=reserva_id,
            codigo_barra=codigo_barra,
            fecha_emision=fecha_emision,
            estado=estado
        )

    @staticmethod
    def obtener_boleto(boleto_id: int) -> Optional[Boleto]:
        return BoletoRepository.get_by_id(boleto_id)

    @staticmethod
    def listar_boletos() -> list[Boleto]:
        return BoletoRepository.get_all()

    @staticmethod
    def buscar_por_codigo(codigo_barra: str) -> Optional[Boleto]:
        return BoletoRepository.get_by_codigo(codigo_barra)

    @staticmethod
    def obtener_por_reserva(reserva_id: int) -> list[Boleto]:
        return BoletoRepository.get_by_reserva(reserva_id)

    @staticmethod
    def obtener_por_estado(estado: str) -> list[Boleto]:
        return BoletoRepository.get_by_estado(estado)
