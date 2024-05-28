from negocio.biblioteca_service import BibliotecaService
from negocio.fabrica_libros import FabricaLibros
from negocio.registro_eventos import RegistroEventos
from negocio.usuario_service import UsuarioService
from presentacion.views import mostrar_menu, obtener_opcion

if __name__ == "__main__":
    biblioteca_service = BibliotecaService()
    biblioteca = RegistroEventos(biblioteca_service)
    fabrica = FabricaLibros()
    usuario_service = UsuarioService(biblioteca_service)

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "1":
            titulo = input("Ingrese el título del libro físico: ")
            autor = input("Ingrese el autor del libro físico: ")
            nuevo_libro = fabrica.crear_libro("fisico", titulo, autor)
            biblioteca.agregar_libro(nuevo_libro)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro electrónico: ")
            autor = input("Ingrese el autor del libro electrónico: ")
            nuevo_libro = fabrica.crear_libro("electronico", titulo, autor)
            biblioteca.agregar_libro(nuevo_libro)
        elif opcion == "3":
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            biblioteca_service.eliminar_libro_por_titulo(titulo)
        elif opcion == "4":
            titulo = input("Ingrese el título del libro que desea prestar: ")
            nombre_usuario = input(
                "Ingrese el nombre del usuario que va a prestar el libro: ")
            usuario_service.prestar_libro(titulo, nombre_usuario)
        elif opcion == "5":
            titulo = input("Ingrese el título del libro que desea devolver: ")
            biblioteca_service.devolver_libro_por_titulo(titulo)
        elif opcion == "6":
            biblioteca.mostrar_libros_disponibles()
        elif opcion == "7":
            print("Registrando usuarios como observadores...")
            num_usuarios = int(
                input("Ingrese el número de usuarios que desea registrar: "))
            for _ in range(num_usuarios):
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                usuario_service.registrar_observador(nombre_usuario)
            print("Usuarios registrados como observadores.")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")
