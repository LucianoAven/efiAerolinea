from typing import Optional
from aerolinea.models import Usuario

class UsuarioRepository:
    """
    Clase que se conecta con la base de datos para manejar usuarios
    """
    @staticmethod
    def create(
        username: str,
        password: str,
        email: str,
        rol: str
    ) -> Usuario:
        """
        Crear un nuevo usuario.
        """
        return Usuario.objects.create(
            username=username,
            password=password,
            email=email,
            rol=rol
        )
    
    @staticmethod
    def delete(usuario: Usuario) -> bool:
        """
        Eliminar un usuario.
        """
        try:
            usuario.delete()
            return True
        except Usuario.DoesNotExist:
            raise ValueError("No se encontró el usuario")

    @staticmethod
    def update(
        usuario: Usuario,
        username: str = None,
        password: str = None,
        email: str = None,
        rol: str = None
    ) -> Usuario:
        """
        Actualizar un usuario
        """
        if username is not None:
            usuario.username = username
        if password is not None:
            usuario.password = password
        if email is not None:
            usuario.email = email
        if rol is not None:
            usuario.rol = rol
            
        usuario.save()
        return usuario

    @staticmethod
    def get_all() -> list[Usuario]:
        """
        Obtener todos los usuarios.
        """
        return Usuario.objects.all()
    
    @staticmethod
    def get_by_id(usuario_id: int) -> Optional[Usuario]:
        """
        Obtener un usuario mediante su id.
        """
        try:
            return Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return None    

    @staticmethod
    def get_by_username(username: str) -> Optional[Usuario]:
        """
        Obtener usuario por nombre de usuario.
        """
        try:
            return Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_email(email: str) -> Optional[Usuario]:
        """
        Obtener usuario por email.
        """
        try:
            return Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_rol(rol: str) -> list[Usuario]:
        """
        Obtener usuarios por rol.
        """
        return Usuario.objects.filter(rol=rol)