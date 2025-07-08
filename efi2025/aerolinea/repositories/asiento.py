
from typing import Optional

from aerolinea.models import Asiento, Avion

class AsientoRepository:

    @staticmethod
    def create(
        avion_id: Avion, 
        numero: int,
        fila: str,
        columna: str,
        tipo: str,
        estado: str
    ) -> Asiento:
        return Asiento.objects.create(
            avion_id=avion_id,
            numero=numero,
            fila=fila,
            columna=columna,
            tipo=tipo,
            estado=estado
        )
  
    @staticmethod
    def delete(asiento_id) -> bool:
        try:
            Asiento.objects.get(id=asiento_id).delete()
        except Asiento.DoesNotExist:
            raise ValueError("No se encontro el asiento")
        
    @staticmethod
    def update(
        asiento: Asiento, 
        avion_id: Avion = None,
        numero: int = None,
        fila: str = None,
        columna: str = None,
        tipo: str = None,
        estado: str = None
    ) -> Asiento:
        """
        Actualizar un asiento
        """
        if avion_id is not None:
            asiento.avion_id = avion_id
        if numero is not None:
            asiento.numero = numero
        if fila is not None:
            asiento.fila = fila
        if columna is not None:
            asiento.columna = columna
        if tipo is not None:
            asiento.tipo = tipo
        if estado is not None:
            asiento.estado = estado
            
        asiento.save()
        return asiento

    @staticmethod
    def get_all() -> list[Asiento]:
        """
        Obtener todos los asientos.
        """
        return Asiento.objects.all()
    
    @staticmethod
    def get_by_id(asiento_id: int) -> Optional[Asiento]:
        """
        Obtener un asiento mediante su id.
        """
        try:
            return Asiento.objects.get(id=asiento_id)
        except Asiento.DoesNotExist:
            return None    
    
    @staticmethod
    def get_by_avion(avion_id: int) -> list[Asiento]:
        """
        Obtener asientos por avión.
        """
        return Asiento.objects.filter(avion_id=avion_id)
    
    @staticmethod
    def get_by_estado(estado: str) -> list[Asiento]:
        """
        Obtener asientos por estado.
        """
        return Asiento.objects.filter(estado=estado)
    
    @staticmethod
    def get_by_tipo(tipo: str) -> list[Asiento]:
        """
        Obtener asientos por tipo.
        """
        return Asiento.objects.filter(tipo=tipo)
