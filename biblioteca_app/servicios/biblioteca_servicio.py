# Importa los modelos existentes en el programa
from modelos.libro import Libro
from modelos.usuario import Usuario

# Clase de servicio que representa la lógica del sistema de gestión de biblioteca virtual
class BibliotecaServicio:

    # Creación de un constructor vacío
    def __init__(self):
        self._libros_disponibles: dict[str, Libro] = {} # Atributo privado que guarda los libros disponibles en un diccionario
        self._usuarios: dict[str, Usuario] = {} # Atributo privado que guarda los usuarios registrados en un diccionario
        self._ids_usuarios: set[str] = set() # Atributo privado que gestiona los IDs únicos de los usuarios en un conjunto
        self._todos_los_libros: dict[str, Libro] = {} # Atributo privado que es el cátalogo completo de todos los libros registrados en un diccionario

    # Método que valida la agregación del libro
    def agregar_libro(self, titulo: str, autor: str, categoria: str, isbn: str) -> tuple[bool, str]:
        # Verifica si el ISBN ya existe
        if isbn in self._todos_los_libros:
            return False, f"Ya existe un libro con ISBN '{isbn}' en el sistema."

        # Se crea un nuevo objeto Libro
        nuevo_libro = Libro(titulo, autor, categoria, isbn)

        # Se agrega a libros disponibles
        self._libros_disponibles[isbn] = nuevo_libro

        # Se agrega al catálogo general
        self._todos_los_libros[isbn] = nuevo_libro

        return True, f"Libro '{titulo}' agregado exitosamente al catálogo 📚."

    # Método que valida la eliminación del libro tras ser devuelto
    def quitar_libro(self, isbn: str) -> tuple[bool, str]:
        # Condicional que verifica si el ISBN existe en el catálogo general de libros
        if isbn not in self._todos_los_libros:
            # Si no existe, se devuelve un mensaje indicando el error
            return False, f"No existe ningún libro con ISBN '{isbn}'."

        # Condicional que verifica si el libro está disponible
        if isbn not in self._libros_disponibles:
            # Si no está disponible significa que está prestado y no se puede eliminar de la lista de prestados
            return False, f"El libro con ISBN '{isbn}' está actualmente prestado y no puede eliminarse😱."

        # Extrae y elimina el libro del diccionario de libros disponibles
        libro = self._libros_disponibles.pop(isbn)

        # También se elimina del catálogo general
        del self._todos_los_libros[isbn]

        # Retorna confirmación de eliminación exitosa
        return True, f"Libro '{libro.titulo}' eliminado del catálogo."

    # Método para registrar un nuevo usuario en la biblioteca
    def registrar_usuario(self, nombre: str, id_usuario: str) -> tuple[bool, str]:
        # Condicional que verifica si el ID ya existe dentro del conjunto de usuarios
        if id_usuario in self._ids_usuarios:
            # Si existe, no se puede registrar nuevamente
            return False, f"Ya existe un usuario con ID '{id_usuario}'."

        # Se crea un nuevo objeto Usuario
        nuevo_usuario = Usuario(nombre, id_usuario)

        # Se guarda en el diccionario de usuarios
        self._usuarios[id_usuario] = nuevo_usuario

        # Se agrega el ID al conjunto para garantizar unicidad
        self._ids_usuarios.add(id_usuario)

        # Retorna confirmación de registro exitoso
        return True, f"Usuario '{nombre}' registrado exitosamente."

    # Método que elimina un usuario del sistema
    def dar_baja_usuario(self, id_usuario: str) -> tuple[bool, str]:
        # Condicional que verifica que el usuario exista
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        # Obtiene el objeto usuario desde el diccionario
        usuario = self._usuarios[id_usuario]

        # Condicional que verifica si el usuario tiene libros prestados
        if usuario.libros_prestados:
            # No se permite eliminar usuarios con libros pendientes
            return False, f"El usuario '{usuario.nombre}' tiene libros pendientes de devolución. No es posible eliminarlo 😥"

        # Elimina al usuario del diccionario de usuarios
        del self._usuarios[id_usuario]

        # Elimina el ID del conjunto de IDs registrados
        self._ids_usuarios.discard(id_usuario)

        # Retorna confirmación de eliminación
        return True, f"Usuario '{usuario.nombre}' dado de baja exitosamente."

    # Método que gestiona el préstamo de un libro a un usuario
    def prestar_libro(self, isbn: str, id_usuario: str) -> tuple[bool, str]:
        # Condicional que verifica que el usuario exista
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        # Condicional que verifica que el libro exista en el catálogo
        if isbn not in self._todos_los_libros:
            return False, f"No existe un libro con ISBN '{isbn}'."

        # Condicional que verifica que el libro esté disponible
        if isbn not in self._libros_disponibles:
            return False, f"El libro con ISBN '{isbn}' no está disponible (ya prestado)😥."

        # Obtiene el objeto usuario
        usuario = self._usuarios[id_usuario]

        # Elimina el libro de los disponibles y lo obtiene
        libro = self._libros_disponibles.pop(isbn)

        # Se agrega el libro a la lista de préstamos del usuario
        usuario._agregar_libro(libro)

        # Retorna confirmación del préstamo
        return True, f"Libro '{libro.titulo}' prestado a '{usuario.nombre}' exitosamente."

    # Método que gestiona la devolución de un libro
    def devolver_libro(self, isbn: str, id_usuario: str) -> tuple[bool, str]:
        # Condicional que verifica que el usuario exista
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        # Obtiene el objeto usuario
        usuario = self._usuarios[id_usuario]

        # Condicional que verifica si el usuario tiene prestado ese libro
        if not usuario.usuario_libro_prestado(isbn):
            return False, f"El usuario '{usuario.nombre}' no tiene prestado el libro con ISBN '{isbn}'😥."

        # Elimina el libro de la lista de préstamos del usuario
        usuario._quitar_libro(isbn)

        # Recupera el libro desde el catálogo general
        libro = self._todos_los_libros[isbn]

        # Vuelve a agregar el libro a los disponibles
        self._libros_disponibles[isbn] = libro

        # Retorna confirmación de devolución
        return True, f"Libro '{libro.titulo}' devuelto exitosamente."

    # Método que busca libros por título
    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        # Convierte el término de búsqueda a minúsculas
        termino = titulo.lower()
        # Recorre todos los libros y devuelve los que coincidan
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.titulo.lower()
        ]

    # Método que busca libros por autor
    def buscar_por_autor(self, autor: str) -> list[Libro]:
        # Convierte el término a minúsculas
        termino = autor.lower()
        # Filtra los libros que contengan ese autor
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.autor.lower()
        ]

    # Método que busca libros por categoría
    def buscar_por_categoria(self, categoria: str) -> list[Libro]:
        # Convierte el término a minúsculas
        termino = categoria.lower()
        # Devuelve los libros cuya categoría coincida
        return [
            libro for libro in self._todos_los_libros.values()
            if termino in libro.categoria.lower()
        ]

    # Método que devuelve los libros prestados a un usuario específico
    def listar_libros_prestados_a_usuario(self, id_usuario: str) -> tuple[bool, list | str]:
        # Condicional que verifica que el usuario exista
        if id_usuario not in self._ids_usuarios:
            return False, f"No existe un usuario con ID '{id_usuario}'."

        # Obtiene el objeto usuario
        usuario = self._usuarios[id_usuario]

        # Obtiene la lista de libros prestados
        prestados = usuario.libros_prestados

        # Devuelve éxito y la lista de libros
        return True, prestados

    # Método que devuelve todos los libros registrados
    def listar_todos_los_libros(self) -> list[Libro]:
        return list(self._todos_los_libros.values())

    # Método que devuelve únicamente los libros disponibles
    def listar_libros_disponibles(self) -> list[Libro]:
        return list(self._libros_disponibles.values())

    # Método que devuelve todos los usuarios registrados
    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios.values())

    # Método que verifica si un libro está disponible para préstamo
    def es_libro_disponible(self, isbn: str) -> bool:
        return isbn in self._libros_disponibles