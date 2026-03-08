from modelos.libro import Libro


class Usuario:

    def __init__(self, nombre: str, id_usuario: str):

        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados: list[Libro] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def id_usuario(self) -> str:
        return self._id_usuario

    @property
    def libros_prestados(self) -> list:
        return list(self._libros_prestados)

    def _agregar_libro(self, libro: Libro) -> None:
        self._libros_prestados.append(libro)

    def _quitar_libro(self, isbn: str) -> bool:
        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return True
        return False

    def tiene_libro(self, isbn: str) -> bool:
        return any(libro.isbn == isbn for libro in self._libros_prestados)

    def __str__(self) -> str:
        cantidad = len(self._libros_prestados)
        return (
            f"  👤 Nombre    : {self.nombre}\n"
            f"     ID        : {self.id_usuario}\n"
            f"     Préstamos : {cantidad} libro(s)"
        )

    def __repr__(self) -> str:
        return f"Usuario(id='{self.id_usuario}', nombre='{self.nombre}')"
