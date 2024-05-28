# Patrón de Comportamiento: Observer
# Implementa la clase BibliotecaObservable que notificará a los observadores
# cuando se agregue un libro a la biblioteca

class BibliotecaObservable:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, libro):
        for observador in self.observadores:
            observador.actualizar(libro)
