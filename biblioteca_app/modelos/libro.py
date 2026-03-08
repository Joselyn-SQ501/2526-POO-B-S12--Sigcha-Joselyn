# Clase que representa un libro dentro del sistema
class Libro:
    # Constructor de la clase con datos y su tipo
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Atributos privados para aplicar encapsulamiento
        self._info = (titulo, autor) # Atributo privado que guarda el título y autor en una tupla (estructura inmutable)
        self._categoria = categoria # Atributo privado que guarda la categoría del libro
        self._isbn = isbn # Atributo privado que guarda el código único de identificación para libros y publicaciones monográficas

    # Getter para obtener el título del libro
    @property
    def titulo(self) -> str:
        return self._info[0] # posición 0 de la tupla
   
    # Getter para obtener el autor del libro
    @property
    def autor(self) -> str:
        return self._info[1] # posición 1 de la tupla

    # Getter que devuelve la información de la tupla completa (titulo, autor)
    @property
    def info(self) -> tuple:
        return self._info

    # Getter de la categoría
    @property
    def categoria(self) -> str:
        return self._categoria

    # Getter del ISBN
    @property
    def isbn(self) -> str:
        return self._isbn

    # Método que define cómo se imprime la información del libro
    def __str__(self) -> str:
        return (
            f"  📖 Título    : {self.titulo}\n"
            f"     Autor     : {self.autor}\n"
            f"     Categoría : {self.categoria}\n"
            f"     ISBN      : {self.isbn}"
        )

    # Método que devuelve la información del libro depurada
    def __repr__(self) -> str:
        return f"Libro(ISBN='{self.isbn}', Título='{self.titulo}', Autor='{self.autor}')"
