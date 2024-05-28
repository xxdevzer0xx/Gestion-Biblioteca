from negocio.libro_electronico import LibroElectronico
from negocio.libro_fisico import LibroFisico


# Patrón Creacional: Factory Method
# este patrón crea instancias de libros. Esto podría permitir la creación de diferentes tipos de libros
# sin especificar las clases concretas, lo que proporciona una gran flexibilidad en el código.
class FabricaLibros:
    def crear_libro(self, tipo, *args, **kwargs):
        # Si el tipo es "fisico", crea una instancia de LibroFisico
        if tipo == "fisico":
            return LibroFisico(*args, **kwargs)
        # Si el tipo es "electronico", crea una instancia de LibroElectronico
        elif tipo == "electronico":
            return LibroElectronico(*args, **kwargs)
        # Si el tipo no es ni "fisico" ni "electronico", lanza un ValueError
        else:
            raise ValueError("Tipo de libro no válido.")
