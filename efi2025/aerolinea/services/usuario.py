
from typing import Optional
from aerolinea.models import Usuario
from .usuario import UsuarioRepository


class UsuarioService:

    @staticmethod
    def crear_usuario(username: str, password: str, email: str, rol: str) -> Usuario:
        return UsuarioRepository.create(username, password, email, rol)

    @staticmethod
    def eliminar_usuario(usuario_id: int) -> bool:
        usuario = UsuarioRepository.get_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        return UsuarioRepository.delete(usuario)

    @staticmethod
    def actualizar_usuario(
        usuario_id: int,
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        rol: Optional[str] = None
    ) -> Usuario:
        usuario = UsuarioRepository.get_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        return UsuarioRepository.update(
            usuario=usuario,
            username=username,
            password=password,
            email=email,
            rol=rol
        )

    @staticmethod
    def obtener_usuario(usuario_id: int) -> Optional[Usuario]:
        return UsuarioRepository.get_by_id(usuario_id)

    @staticmethod
    def listar_usuarios() -> list[Usuario]:
        return UsuarioRepository.get_all()

    @staticmethod
    def obtener_por_username(username: str) -> Optional[Usuario]:
        return UsuarioRepository.get_by_username(username)

    @staticmethod
    def obtener_por_email(email: str) -> Optional[Usuario]:
        return UsuarioRepository.get_by_email(email)

    @staticmethod
    def obtener_por_rol(rol: str) -> list[Usuario]:
        return UsuarioRepository.get_by_rol(rol)
