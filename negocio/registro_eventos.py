# Patron Decorador
# RegistroEventos es un decorador para la clase gestor_biblioteca.
# Añade funcionalidades de registro de eventos a los métodos agregar_libro, eliminar_libro y mostrar_libros_disponibles
# sin modificar la implementación original de estos métodos.
class RegistroEventos:
    def __init__(self, gestor_biblioteca):
        self.gestor_biblioteca = gestor_biblioteca

    def agregar_libro(self, libro):
        print(f"Evento: Se agregó el libro {libro.titulo} a la biblioteca.")
        self.gestor_biblioteca.agregar_libro(libro)

    def eliminar_libro(self, libro):
        print(f"Evento: Se eliminó el libro {libro.titulo} de la biblioteca.")
        self.gestor_biblioteca.eliminar_libro(libro)

    def mostrar_libros_disponibles(self):
        self.gestor_biblioteca.mostrar_libros_disponibles()
