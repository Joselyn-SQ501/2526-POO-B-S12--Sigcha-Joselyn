# Importa la clase libro para poder usar sus atributos
from modelos.libro import Libro

# Clase que representa un usuario registrado en la biblioteca
class Usuario:

    # Constructor de la clase con datos y su tipo de dato
    def __init__(self, nombre: str, id_usuario: str):
        # Atributos privados para aplicar encapsulamiento
        self._nombre = nombre # Atributo privado que guarda el nombre del usuario
        self._id_usuario = id_usuario # Atributo privado que guarda el id del usuario
        self._libros_prestados: list[Libro] = [] # Atributo privado que guarda los libros prestados en una lista

    # Método getter del nombre del usuario
    @property
    def nombre(self) -> str:
        return self._nombre

    # Método getter del id del usuario
    @property
    def id_usuario(self) -> str:
        return self._id_usuario

    # Método getter de la lista de los libros prestados
    @property
    def libros_prestados(self) -> list:
        return list(self._libros_prestados)

    # Método para agregar un libro a la lista de libros prestados
    def _agregar_libro(self, libro: Libro) -> None:
        self._libros_prestados.append(libro)

    # Método para eliminar o quitar un libro de la lista de libros prestados cuando es devuelto
    def _quitar_libro(self, isbn: str) -> bool:
        # Bucle for que recorre todos los libros prestados
        for libro in self._libros_prestados:
            # Condicional que encuentra el ISBN solicitado
            if libro.isbn == isbn:
                # Al encontrar el ISBN lo elimina de la lista
                self._libros_prestados.remove(libro)
                return True
        return False # Si no encuentra el libro

    # Método que verifica si un usuario tiene un libro prestado
    def usuario_libro_prestado (self, isbn: str) -> bool:
        # Devuelve True si alguno cumple la condición
        return any(libro.isbn == isbn for libro in self._libros_prestados)

    # Método que define cómo se imprime la información del usuario y los libros prestados a él/ella
    def __str__(self) -> str:
        # Número de libros prestados
        cantidad = len(self._libros_prestados)
        return (
            f"  👤 Nombre    : {self.nombre}\n"
            f"     ID        : {self.id_usuario}\n"
            f"     Préstamos : {cantidad} libro(s)"
        )

    # Método que devuelve la información del usuario
    def __repr__(self) -> str:
        return f"Usuario (Id='{self.id_usuario}', Nombre='{self.nombre}')"
