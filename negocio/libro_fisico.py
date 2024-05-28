from negocio.libro import Libro


# Open/Closed Principle (OCP):
# La subclase LibroFisicopueden ser usada en lugar de la clase base (Libro)
# sin alterar el comportamiento del programa.
class LibroFisico(Libro):
    pass
