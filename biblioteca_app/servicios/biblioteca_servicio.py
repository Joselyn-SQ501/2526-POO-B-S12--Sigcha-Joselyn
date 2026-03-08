from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):
        self._libros_disponibles: dict[str, Libro] = {}
        self._usuarios: dict[str, Usuario] = {}
        self._ids_usuarios: set[str] = set()
        self._todos_los_libros: dict[str, Libro] = {}

    def agregar_libro(self, titulo: str, autor: str, categoria: str, isbn: str) -> tuple[bool, str]:
        if isbn in self._todos_los_libros:
            return False, f"Ya existe un libro con ISBN '{isbn}' en el sistema."

        nuevo_libro = Libro(titulo, autor, categoria, isbn)
        self._libros_disponibles[isbn] = nuevo_libro
        self._todos_los_libros[isbn] = nuevo_libro
        return True, f"Libro '{titulo}' agregado exitosamente al catálogo."

    def quitar_libro(self, isbn: str) -> tuple[bool, str]:
        if isbn not in self._todos_los_libros:
            return False, f"No existe ningún libro con ISBN '{isbn}'."

        if isbn not in self._libros_disponibles:
            return False, f"El libro con ISBN '{isbn}' está actualmente prestado y no puede eliminarse."

        libro = self._libros_disponibles.pop(isbn)
        del self._todos_los_libros[isbn]
        return True, f"Libro '{libro.titulo}' eliminado del catálogo."

    def registrar_usuario(self, nombre: str, id_usuario: str) -> tuple[bool, str]:
        if id_usuario in self._ids_usuarios:
            return False, f"Ya existe un usuario con ID '{id_usuario}'."

        nuevo_usuario = Usuario(nombre, id_usuario)
        self._usuarios[id_usuario] = nuevo_usuario
        self._ids_usuarios.add(id_usuario)
        return True, f"Usuario '{nombre}' registrado exitosamente."

    def dar_baja_usuario(self, id_usuario: str) -> tuple[bool, str]:
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        usuario = self._usuarios[id_usuario]
        if usuario.libros_prestados:
            return False, f"El usuario '{usuario.nombre}' tiene libros pendientes de devolución."

        del self._usuarios[id_usuario]
        self._ids_usuarios.discard(id_usuario)
        return True, f"Usuario '{usuario.nombre}' dado de baja exitosamente."

    def prestar_libro(self, isbn: str, id_usuario: str) -> tuple[bool, str]:
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        if isbn not in self._todos_los_libros:
            return False, f"No existe un libro con ISBN '{isbn}'."

        if isbn not in self._libros_disponibles:
            return False, f"El libro con ISBN '{isbn}' no está disponible (ya prestado)."

        usuario = self._usuarios[id_usuario]
        libro = self._libros_disponibles.pop(isbn)
        usuario._agregar_libro(libro)
        return True, f"Libro '{libro.titulo}' prestado a '{usuario.nombre}' exitosamente."

    def devolver_libro(self, isbn: str, id_usuario: str) -> tuple[bool, str]:
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        usuario = self._usuarios[id_usuario]

        if not usuario.tiene_libro(isbn):
            return False, f"El usuario '{usuario.nombre}' no tiene prestado el libro con ISBN '{isbn}'."

        usuario._quitar_libro(isbn)
        libro = self._todos_los_libros[isbn]
        self._libros_disponibles[isbn] = libro
        return True, f"Libro '{libro.titulo}' devuelto exitosamente."

    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        termino = titulo.lower()
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.titulo.lower()
        ]

    def buscar_por_autor(self, autor: str) -> list[Libro]:
        termino = autor.lower()
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.autor.lower()
        ]

    def buscar_por_categoria(self, categoria: str) -> list[Libro]:
        termino = categoria.lower()
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.categoria.lower()
        ]

    def listar_libros_prestados_a_usuario(self, id_usuario: str) -> tuple[bool, list | str]:
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        usuario = self._usuarios[id_usuario]
        prestados = usuario.libros_prestados
        return True, prestados

    def listar_todos_los_libros(self) -> list[Libro]:
        return list(self._todos_los_libros.values())

    def listar_libros_disponibles(self) -> list[Libro]:
        return list(self._libros_disponibles.values())

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios.values())

    def es_libro_disponible(self, isbn: str) -> bool:
        return isbn in self._libros_disponibles