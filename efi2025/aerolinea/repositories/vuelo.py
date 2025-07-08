from typing import Optional
from aerolinea.models import Vuelo, Avion
from django.utils.translation import gettext_lazy as _

class VueloRepository:
    """
    Clase que se conecta con la base de datos para manejar vuelos
    """
    @staticmethod
    def create(
        avion_id: Avion,
        origen: str,
        destino: str,
        fecha_salida: str,
        fecha_llegada: str,
        duracion: str,
        estado: str,
        precio_base: float
    ) -> Vuelo:
        """
        Crear un nuevo vuelo.
        """
        return Vuelo.objects.create(
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
    def delete(vuelo: Vuelo) -> bool:
        """
        Eliminar un vuelo.
        """
        try:
            vuelo.delete()
            return True
        except Vuelo.DoesNotExist:
            raise ValueError("No se encontró el vuelo")

    @staticmethod
    def update(
        vuelo: Vuelo,
        avion_id: Avion = None,
        origen: str = None,
        destino: str = None,
        fecha_salida: str = None,
        fecha_llegada: str = None,
        duracion: str = None,
        estado: str = None,
        precio_base: float = None
    ) -> Vuelo:
        """
        Actualizar un vuelo
        """
        if avion_id is not None:
            vuelo.avion_id = avion_id
        if origen is not None:
            vuelo.origen = origen
        if destino is not None:
            vuelo.destino = destino
        if fecha_salida is not None:
            vuelo.fecha_salida = fecha_salida
        if fecha_llegada is not None:
            vuelo.fecha_llegada = fecha_llegada
        if duracion is not None:
            vuelo.duracion = duracion
        if estado is not None:
            vuelo.estado = estado
        if precio_base is not None:
            vuelo.precio_base = precio_base
            
        vuelo.save()
        return vuelo

    @staticmethod
    def get_all() -> list[Vuelo]:
        """
        Obtener todos los vuelos.
        """
        return Vuelo.objects.all()
    
    @staticmethod
    def get_by_id(vuelo_id: int) -> Optional[Vuelo]:
        """
        Obtener un vuelo mediante su id.
        """
        try:
            return Vuelo.objects.get(id=vuelo_id)
        except Vuelo.DoesNotExist:
            return None    

    @staticmethod
    def search_by_destino(destino: str) -> list[Vuelo]:
        """
        Buscar vuelos que coincidan con el destino ingresado.
        """
        return Vuelo.objects.filter(destino__icontains=destino)
    
    @staticmethod
    def filter_by_fecha_range(fecha_inicio: str, fecha_fin: str) -> list[Vuelo]:
        """
        Filtrar vuelos por rango de fechas.
        """
        return Vuelo.objects.filter(fecha_salida__range=(fecha_inicio, fecha_fin))