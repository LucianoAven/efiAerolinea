
from typing import Optional
from aerolinea.models import Pasajero
from repositories.pasajero import PasajeroRepository

class PasajeroService:

    @staticmethod
    def crear_pasajero(nombre: str, documento: int, email: str, telefono: str, fecha_nacimiento: str, tipo_documento: str) -> Pasajero:
        return PasajeroRepository.create(nombre, documento, email, telefono, fecha_nacimiento, tipo_documento)

    @staticmethod
    def eliminar_pasajero(pasajero_id: int) -> bool:
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if not pasajero:
            raise ValueError("Pasajero no encontrado")
        return PasajeroRepository.delete(pasajero)

    @staticmethod
    def actualizar_pasajero(
        pasajero_id: int,
        nombre: Optional[str] = None,
        documento: Optional[int] = None,
        email: Optional[str] = None,
        telefono: Optional[str] = None,
        fecha_nacimiento: Optional[str] = None,
        tipo_documento: Optional[str] = None
    ) -> Pasajero:
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if not pasajero:
            raise ValueError("Pasajero no encontrado")
        return PasajeroRepository.update(
            pasajero=pasajero,
            nombre=nombre,
            documento=documento,
            email=email,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            tipo_documento=tipo_documento
        )


    @staticmethod
    def obtener_pasajero(pasajero_id: int) -> Optional[Pasajero]:
        return PasajeroRepository.get_by_id(pasajero_id)

    @staticmethod
    def listar_pasajeros() -> list[Pasajero]:
        return PasajeroRepository.get_all()

    @staticmethod
    def buscar_por_nombre(nombre: str) -> list[Pasajero]:
        return PasajeroRepository.search_by_nombre(nombre)

    @staticmethod
    def obtener_por_email(email: str) -> Optional[Pasajero]:
        return PasajeroRepository.get_by_email(email)
