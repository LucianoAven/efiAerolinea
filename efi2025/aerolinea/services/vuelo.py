
from typing import Optional
from aerolinea.models import Vuelo, Avion
from repositories.vuelo import VueloRepository


class VueloService:
    """
    Servicio para gestionar los vuelos.
    """

    @staticmethod
    def crear_vuelo(
        avion_id: Avion,
        origen: str,
        destino: str,
        fecha_salida: str,
        fecha_llegada: str,
        duracion: str,
        estado: str,
        precio_base: float
    ) -> Vuelo:
        return VueloRepository.create(
            avion_id=avion_id,
            origen=origen,
            destino=destino,
            fecha_salida=fecha_salida,
            fecha_llegada=fecha_llegada,
            duracion=duracion,
            estado=estado,
            precio_base=precio_base
        )

    @staticmethod
    def eliminar_vuelo(vuelo_id: int) -> bool:
        vuelo = VueloRepository.get_by_id(vuelo_id)
        if not vuelo:
            raise ValueError("Vuelo no encontrado")
        return VueloRepository.delete(vuelo)

    @staticmethod
    def actualizar_vuelo(
        vuelo_id: int,
        avion_id: Optional[Avion] = None,
        origen: Optional[str] = None,
        destino: Optional[str] = None,
        fecha_salida: Optional[str] = None,
        fecha_llegada: Optional[str] = None,
        duracion: Optional[str] = None,
        estado: Optional[str] = None,
        precio_base: Optional[float] = None
    ) -> Vuelo:
        vuelo = VueloRepository.get_by_id(vuelo_id)
        if not vuelo:
            raise ValueError("Vuelo no encontrado")

        return VueloRepository.update(
            vuelo,
            avion_id=avion_id,
            origen=origen,
            destino=destino,
            fecha_salida=fecha_salida,
            fecha_llegada=fecha_llegada,
            duracion=duracion,
            estado=estado,
            precio_base=precio_base
        )

    @staticmethod
    def obtener_vuelo(vuelo_id: int) -> Optional[Vuelo]:
        return VueloRepository.get_by_id(vuelo_id)

    @staticmethod
    def listar_vuelos() -> list[Vuelo]:
        return VueloRepository.get_all()

    @staticmethod
    def buscar_por_destino(destino: str) -> list[Vuelo]:
        return VueloRepository.search_by_destino(destino)

    @staticmethod
    def filtrar_por_rango_fechas(fecha_inicio: str, fecha_fin: str) -> list[Vuelo]:
        return VueloRepository.filter_by_fecha_range(fecha_inicio, fecha_fin)
