class Libro:

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):

        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn


    @property
    def titulo(self) -> str:
        return self._info[0]

    @property
    def autor(self) -> str:
        return self._info[1]

    @property
    def info(self) -> tuple:
        return self._info

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def isbn(self) -> str:
        return self._isbn

    def __str__(self) -> str:
        return (
            f"  📖 Título    : {self.titulo}\n"
            f"     Autor     : {self.autor}\n"
            f"     Categoría : {self.categoria}\n"
            f"     ISBN      : {self.isbn}"
        )

    def __repr__(self) -> str:
        return f"Libro(isbn='{self.isbn}', titulo='{self.titulo}', autor='{self.autor}')"
