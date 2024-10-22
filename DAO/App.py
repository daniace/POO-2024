import sqlite3
from sqlite3 import Error

from Usuario import Usuario
from UsuarioDAOImp import UsuarioDAOImp

try:
    conexion = sqlite3.connect("mibasededatos.db")

    usuario_dao = UsuarioDAOImp(conexion)

    # Insertar un usuario
    nuevo_usuario = Usuario(0, "Juan", "juan@email.com")
    usuario_dao.insertar_usuario(nuevo_usuario)

    # Obtener un usuario por su id
    usuarios = usuario_dao.obtener_todos_los_usuarios()
    for usuario in usuarios:
        print(usuario)

    # Actualizar un usuario
    usuario_actualizado = usuarios[0]
    usuario_actualizado.set_nombre("Juan Actualizado")
    usuario_dao.actualizar_usuario(usuario_actualizado)

    # Obtener un usuario por su id
    usuario_por_id = usuario_dao.obtener_usuario_por_id(usuario_actualizado.get_id())
    print("Usuario obtenido por id:", usuario_por_id)

    # Eliminar un usuario por su id
    usuario_dao.eliminar_usuario(usuario_actualizado.get_id())

except Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    conexion.close()
    print("Conexión cerrada")
