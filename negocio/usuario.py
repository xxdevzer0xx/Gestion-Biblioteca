class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, libro):
        print(f"¡Notificación para {self.nombre}: El libro {
              libro.titulo} está disponible nuevamente!")
