from datos.biblioteca_repository import BibliotecaRepository
from negocio.biblioteca_observable import BibliotecaObservable

from .libro_fisico import LibroFisico


class BibliotecaService(BibliotecaObservable):
    def __init__(self):
        super().__init__()
        self.repo = BibliotecaRepository()
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.repo.agregar_libro(libro)
        self.libros.append(libro)
        print(f"Libro añadido: {libro.titulo}")
        self.notificar_observadores(libro)

    def eliminar_libro_por_titulo(self, titulo):
        libro = self.repo.obtener_libro_por_titulo(titulo)
        if libro:
            self.repo.eliminar_libro(libro)
            print(f"Libro eliminado: {libro.titulo}")
            self.libros.remove(libro)
        else:
            print("El libro no se encuentra en la biblioteca.")

    def prestar_libro_por_titulo(self, titulo, usuario):
        libro = self.repo.obtener_libro_por_titulo(titulo)
        if libro:
            libro.prestar()
            usuario.actualizar(libro)
            print(f"Libro {libro.titulo} prestado a {usuario.nombre}")
            self.libros_prestados.append(libro)
        else:
            print("El libro no se encuentra en la biblioteca.")

    def devolver_libro_por_titulo(self, titulo):
        libro = self.repo.obtener_libro_por_titulo(titulo)
        if libro:
            libro.devolver()
            print(f"Libro {libro.titulo} devuelto")
            if libro in self.libros_prestados:
                self.libros_prestados.remove(libro)
        else:
            print("El libro no se encuentra en la biblioteca.")

    def mostrar_libros_disponibles(self):
        print("\n--- Libros Disponibles ---")
        for libro in self.libros:
            if libro not in self.libros_prestados:
                tipo = "Físico" if isinstance(
                    libro, LibroFisico) else "Electrónico"
                print(f"- {libro.titulo}  por {libro.autor} ({tipo})")
