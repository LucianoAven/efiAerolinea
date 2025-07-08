
from typing import Optional
from aerolinea.models import Avion
from aerolinea.repositories.avion import AvionRepository


class AvionService:
    """
    Servicio que gestiona la lógica de negocio para los aviones.
    """

    @staticmethod
    def crear_avion(
        modelo: str,
        capacidad: int,
        filas: int,
        columnas: int
    ) -> Avion:
        return AvionRepository.create(
            modelo=modelo,
            capacidad=capacidad,
            filas=filas,
            columnas=columnas
        )

    @staticmethod
    def eliminar_avion(avion_id: int) -> bool:
        avion = AvionRepository.get_by_id(avion_id)
        if not avion:
            raise ValueError("Avión no encontrado")
        return AvionRepository.delete(avion_id)

    @staticmethod
    def actualizar_avion(
        avion_id: int,
        capacidad: int,
        filas: int,
        columnas: int
    ) -> Avion:
        avion = AvionRepository.get_by_id(avion_id)
        if not avion:
            raise ValueError("Avión no encontrado")

        return AvionRepository.update(
            avion=avion,
            capacidad=capacidad,
            filas=filas,
            columnas=columnas
        )

    @staticmethod
    def obtener_avion(avion_id: int) -> Optional[Avion]:
        return AvionRepository.get_by_id(avion_id)

    @staticmethod
    def listar_aviones() -> list[Avion]:
        return AvionRepository.get_all()

    @staticmethod
    def buscar_por_modelo(modelo: str) -> list[Avion]:
        return AvionRepository.search_by_modelo(modelo)

    @staticmethod
    def filtrar_por_rango_capacidad(min_capacidad: int, max_capacidad: int) -> list[Avion]:
        return AvionRepository.filter_by_capacidad_range(min_capacidad, max_capacidad)

