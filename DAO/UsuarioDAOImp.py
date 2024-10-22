from sqlite3 import Error
from typing import List

from Usuario import Usuario


class UsuarioDAOImp:
    """Clase que implementa la interfaz UsuarioDAO"""

    def __init__(self, conexion) -> None:
        self.__conexion = conexion

    def obtener_usuario_por_id(self, id: int) -> Usuario | None:
        """Devuelve un usuario por su id"""
        usuario = None
        query = "SELECT * FROM usuario WHERE id = ?"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row is not None:
                usuario = Usuario(row[0], row[1], row[2])
        except Error as e:
            print("Error al obtener el usuario por id:", e)
        return usuario

    def obtener_todos_los_usuarios(self) -> list[Usuario]:
        """Devuelve todos los usuarios"""
        usuarios: list[Usuario] = []
        query = "SELECT * FROM usuario"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                usuario = Usuario(row[0], row[1], row[2])
                usuarios.append(usuario)
        except Error as e:
            print("Error al obtener todos los usuarios:", e)
        return usuarios

    def insertar_usuario(self, usuario: Usuario) -> None:
        """Inserta un usuario"""
        query = "INSERT INTO usuario (nombre, email) VALUES (?, ?)"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (usuario.get_nombre(), usuario.get_email()))
            self.__conexion.commit()
        except Error as e:
            print("Error al insertar el usuario:", e)

    def actualizar_usuario(self, usuario: Usuario) -> None:
        """Actualiza un usuario"""
        query = "UPDATE usuario SET nombre = ?, email = ? WHERE id = ?"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(
                query, (usuario.get_nombre(), usuario.get_email(), usuario.get_id())
            )
            self.__conexion.commit()
        except Error as e:
            print("Error al actualizar el usuario:", e)

    def eliminar_usuario(self, id: int) -> None:
        """Elimina un usuario por su id"""
        query = "DELETE FROM usuario WHERE id = ?"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (id,))
            self.__conexion.commit()
        except Error as e:
            print("Error al eliminar el usuario:", e)
