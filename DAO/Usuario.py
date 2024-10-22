class Usuario:
    """Clase Usuario"""

    def __init__(self, id, nombre, email) -> None:
        self.__id: int = id
        self.__nombre: str = nombre
        self.__email: str = email

    # Getters y Setters
    def get_id(self) -> int:
        """Devuelve el id del usuario"""
        return self.__id

    def set_id(self, id) -> None:
        """Establece el id del usuario"""
        self.__id = id

    def get_nombre(self) -> str:
        """Devuelve el nombre del usuario"""
        return self.__nombre

    def set_nombre(self, nombre) -> None:
        """Establece el nombre del usuario"""
        self.__nombre = nombre

    def get_email(self) -> str:
        """Devuelve el email del usuario"""
        return self.__email

    def set_email(self, email) -> None:
        """Establece el email del usuario"""
        self.__email = email

    def __str__(self) -> str:
        return f"Usuario [id={self.__id}, nombre={self.__nombre}, email={self.__email}]"
