from typing import Optional

from aerolinea.models import Avion


class AvionRepository:

    @staticmethod
    def create(
        modelo: str, 
        capacidad: int,
        filas: int,
        columnas: int
    ) -> Avion:
        return Avion.objects.create(
            modelo=modelo,
            capacidad=capacidad,
            filas=filas,
            columnas=columnas
        )


    @staticmethod
    def delete(avion_id) -> bool:
        try:
            Avion.objects.get(id=avion_id).delete()
        except Avion.DoesNotExist:
            raise ValueError("El avion no existe")
   
   
    @staticmethod
    def update(avion: Avion, capacidad: int, filas: int, columnas: int) -> Avion:
        avion.capacidad = capacidad
        avion.filas = filas
        avion.columnas = columnas
        avion.save()

        return avion


    @staticmethod
    def get_all() -> list[Avion]:
        return Avion.objects.all()
    
    
    @staticmethod
    def get_by_id(avion_id: int) -> Optional[Avion]:
        """
        Obtener un avión mediante su id.
        """
        try:
            return Avion.objects.get(id=avion_id)
        except Avion.DoesNotExist:
            return None    

    
    @staticmethod
    def search_by_modelo(modelo: str) -> list[Avion]:
        return Avion.objects.filter(modelo__icontains=modelo)


    @staticmethod
    def filter_by_capacidad_range(min_capacidad: int, max_capacidad: int) -> list[Avion]:
        return Avion.objects.filter(capacidad__range=(min_capacidad, max_capacidad))

    