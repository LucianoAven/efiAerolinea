
from typing import Optional
from aerolinea.models import Asiento, Avion
from repositories.asiento import AsientoRepository

class AsientoService:

    @staticmethod
    def crear_asiento(
        avion_id: Avion,
        numero: int,
        fila: str,
        columna: str,
        tipo: str,
        estado: str
    ) -> Asiento:
        return AsientoRepository.create(
            avion_id=avion_id,
            numero=numero,
            fila=fila,
            columna=columna,
            tipo=tipo,
            estado=estado
        )

    @staticmethod
    def eliminar_asiento(asiento_id: int) -> bool:
        asiento = AsientoRepository.get_by_id(asiento_id)
        if not asiento:
            raise ValueError("El asiento no existe")
        AsientoRepository.delete(asiento_id)
        return True

    @staticmethod
    def actualizar_asiento(
        asiento_id: int,
        avion_id: Optional[Avion] = None,
        numero: Optional[int] = None,
        fila: Optional[str] = None,
        columna: Optional[str] = None,
        tipo: Optional[str] = None,
        estado: Optional[str] = None
    ) -> Asiento:
        asiento = AsientoRepository.get_by_id(asiento_id)
        if not asiento:
            raise ValueError("Asiento no encontrado")

        return AsientoRepository.update(
            asiento,
            avion_id=avion_id,
            numero=numero,
            fila=fila,
            columna=columna,
            tipo=tipo,
            estado=estado
        )

    @staticmethod
    def obtener_asiento(asiento_id: int) -> Optional[Asiento]:
        return AsientoRepository.get_by_id(asiento_id)

    @staticmethod
    def listar_asientos() -> list[Asiento]:
        return AsientoRepository.get_all()

    @staticmethod
    def obtener_asientos_por_avion(avion_id: int) -> list[Asiento]:
        return AsientoRepository.get_by_avion(avion_id)

    @staticmethod
    def obtener_asientos_por_estado(estado: str) -> list[Asiento]:
        return AsientoRepository.get_by_estado(estado)

    @staticmethod
    def obtener_asientos_por_tipo(tipo: str) -> list[Asiento]:
        return AsientoRepository.get_by_tipo(tipo)
