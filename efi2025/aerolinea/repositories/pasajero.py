from typing import Optional
from aerolinea.models import Pasajero

class PasajeroRepository:
    """
    Clase que se conecta con la base de datos para manejar pasajeros
    """
    @staticmethod
    def create(
        nombre: str,
        documento: int,
        email: str,
        telefono: str,
        fecha_nacimiento: str,
        tipo_documento: str
    ) -> Pasajero:
        """
        Crear un nuevo pasajero.
        """
        return Pasajero.objects.create(
            nombre=nombre,
            documento=documento,
            email=email,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            tipo_documento=tipo_documento
        )
    
    @staticmethod
    def delete(pasajero: Pasajero) -> bool:
        """
        Eliminar un pasajero.
        """
        try:
            pasajero.delete()
            return True
        except Pasajero.DoesNotExist:
            raise ValueError("No se encontró el pasajero")

    @staticmethod
    def update(
        pasajero: Pasajero,
        nombre: str = None,
        documento: int = None,
        email: str = None,
        telefono: str = None,
        fecha_nacimiento: str = None,
        tipo_documento: str = None
    ) -> Pasajero:
        """
        Actualizar un pasajero
        """
        if nombre is not None:
            pasajero.nombre = nombre
        if documento is not None:
            pasajero.documento = documento
        if email is not None:
            pasajero.email = email
        if telefono is not None:
            pasajero.telefono = telefono
        if fecha_nacimiento is not None:
            pasajero.fecha_nacimiento = fecha_nacimiento
        if tipo_documento is not None:
            pasajero.tipo_documento = tipo_documento
            
        pasajero.save()
        return pasajero

    @staticmethod
    def get_all() -> list[Pasajero]:
        """
        Obtener todos los pasajeros.
        """
        return Pasajero.objects.all()
    
    @staticmethod
    def get_by_id(pasajero_id: int) -> Optional[Pasajero]:
        """
        Obtener un pasajero mediante su id.
        """
        try:
            return Pasajero.objects.get(id=pasajero_id)
        except Pasajero.DoesNotExist:
            return None    

    @staticmethod
    def search_by_nombre(nombre: str) -> list[Pasajero]:
        """
        Buscar pasajeros que coincidan con el nombre ingresado.
        """
        return Pasajero.objects.filter(nombre__icontains=nombre)
    
    @staticmethod
    def get_by_email(email: str) -> Optional[Pasajero]:
        """
        Obtener pasajero por email.
        """
        try:
            return Pasajero.objects.get(email=email)
        except Pasajero.DoesNotExist:
            return None