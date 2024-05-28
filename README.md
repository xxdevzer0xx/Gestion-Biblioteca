# Gestion-Biblioteca

Descripción

Este proyecto es un sistema de gestión de biblioteca diseñado para gestionar múltiples aspectos como el catálogo de libros, la gestión de membresías, los préstamos y devoluciones, y las recomendaciones de lectura. El objetivo es proporcionar un sistema robusto y eficiente utilizando buenas prácticas de ingeniería de software cumpliendo con los principios SOLID, varios patrones de diseño y una arquitectura de 3 capas para garantizar un código mantenible, extensible y escalable.

Características

- Gestión de catálogo de libros.
- Administración de membresías.
- Sistema de préstamos y devoluciones.
- Recomendaciones de lectura personalizadas.
- Gestión de eventos y talleres.

Arquitectura

El sistema sigue una arquitectura de 3 capas:

Capa de Presentación: Maneja la interfaz de usuario y las interacciones con el usuario.

Capa de Negocio: Contiene la lógica de negocio y las reglas del sistema.

Capa de Datos: Gestiona el acceso a la base de datos y las operaciones de persistencia.

Principios SOLID

S - Responsabilidad Única (Single Responsibility Principle)
Cada clase tiene una única responsabilidad. Por ejemplo, la clase CatalogService se encarga solo de las operaciones relacionadas con el catálogo de libros.

O - Abierto/Cerrado (Open/Closed Principle)
El sistema está diseñado para ser extensible sin modificar el código existente. Por ejemplo, el patrón de diseño Strategy se utiliza para las recomendaciones de lectura, permitiendo agregar nuevos algoritmos de recomendación sin cambiar los existentes.

L - Sustitución de Liskov (Liskov Substitution Principle)
Las clases derivadas pueden ser sustituidas por sus clases base sin alterar el comportamiento correcto del programa.

I - Segregación de Interfaces (Interface Segregation Principle)
Se crean interfaces específicas de clientes, evitando interfaces grandes y monolíticas. Por ejemplo, IBookRepository y IMembershipRepository.

D - Inversión de Dependencias (Dependency Inversion Principle)
El sistema depende de abstracciones y no de concretos. Las dependencias son inyectadas, permitiendo un desacoplamiento fuerte entre las clases.

Patrones de Diseño

Singleton
Usado para la conexión a la base de datos, asegurando que solo exista una instancia de la conexión a lo largo del ciclo de vida de la aplicación.

Strategy
Implementado en el servicio de recomendaciones de lectura para permitir diferentes algoritmos de recomendación.

Repository
Usado para la abstracción de la capa de datos, proporcionando una interfaz limpia para las operaciones de acceso a la base de datos.

Factory
Utilizado para la creación de objetos, especialmente en la capa de negocio para gestionar las diversas estrategias de recomendación.

Requisitos
  Python 3.x

Instalación
  1. Clona el repositorio
     git clone https://github.com/xxdevzer0xx/Gestion-Biblioteca.git
  2. Navega al directorio del proyecto
     Gestion-Biblioteca
     
Ejecución
  Para ejecutar la aplicación, simplemente ejecuta el archivo main.py desde consola
  python -m presentacion.main

Uso
  Al ejecutar la aplicación, se mostrará un menú de opciones:
  
--- MENÚ DE OPCIONES ---
1. Agregar libro físico
2. Agregar libro electrónico
3. Eliminar libro
4. Prestar libro
5. Devolver libro
6. Mostrar libros disponibles
7. Registrar usuarios como observadores
8. Salir

Sigue las instrucciones en pantalla para interactuar con la biblioteca.

Ejemplo de Uso:

Agregar un Libro Físico
Selecciona la opción 1 en el menú.
Ingresa el título y el autor del libro cuando se te solicite.

Prestar un Libro
Selecciona la opción 4 en el menú.
Ingresa el título del libro que deseas prestar.
Ingresa el nombre del usuario que prestará el libro.

Devolver un Libro
Selecciona la opción 5 en el menú.
Ingresa el título del libro que deseas devolver.

Mostrar Libros Disponibles
Selecciona la opción 6 en el menú para ver una lista de libros disponibles.

Registrar Usuarios como Observadores
Selecciona la opción 7 en el menú.
Ingresa el número de usuarios que deseas registrar y sus nombres.



