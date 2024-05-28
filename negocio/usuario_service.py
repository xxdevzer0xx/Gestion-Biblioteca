from negocio.usuario import Usuario


class UsuarioService:
    def __init__(self, biblioteca_service):
        self.biblioteca_service = biblioteca_service

    def prestar_libro(self, titulo, nombre_usuario):
        usuario = Usuario(nombre_usuario)
        self.biblioteca_service.prestar_libro_por_titulo(titulo, usuario)

    def registrar_observador(self, nombre_usuario):
        usuario = Usuario(nombre_usuario)
        self.biblioteca_service.agregar_observador(usuario)
