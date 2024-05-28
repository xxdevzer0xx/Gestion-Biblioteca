class BibliotecaRepository:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def obtener_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
