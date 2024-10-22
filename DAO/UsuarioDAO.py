from abc import ABC, abstractmethod


class UsuarioDAO(ABC):
    """Interfaz que define los métodos que debe implementar un DAO de Usuario"""

    @abstractmethod
    def obtener_usuario_por_id(self, id: int):
        """Devuelve un usuario por su id"""

    @abstractmethod
    def obtener_todos_los_usuarios(self):
        """Devuelve todos los usuarios"""

    @abstractmethod
    def insertar_usuario(self, usuario):
        """Inserta un usuario"""

    @abstractmethod
    def actualizar_usuario(self, usuario):
        """Actualiza un usuario"""

    @abstractmethod
    def eliminar_usuario(self, id):
        """Elimina un usuario por su id"""
