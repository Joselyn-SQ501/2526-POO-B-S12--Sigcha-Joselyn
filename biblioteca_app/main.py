# Importa el módulo sys para interactuar con el sistema de Python
import sys
# Importa el módulo os para utilizar funciones del sistema operativo
import os

"""
Sistema de Gestión de Biblioteca Digital.

Este programa permite administrar una biblioteca digital utilizando
Programación Orientada a Objetos (POO) y una arquitectura por capas.
El sistema gestiona libros, usuarios y préstamos, permitiendo realizar
operaciones como agregar o eliminar libros, registrar usuarios,
realizar préstamos y devoluciones, y buscar libros por título,
autor o categoría.

Para su funcionamiento utiliza diferentes estructuras de datos o colecciones
como tuplas, listas, diccionarios y conjuntos, organizando la lógica del
sistema en modelos y servicios, mientras que el archivo main.py se
encarga de la interacción con el usuario mediante un menú en consola.
"""

# Agrega la ruta del directorio actual al sistema de búsqueda de módulos
# Esto permite que Python pueda encontrar correctamente las carpetas "modelos" y "servicios"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Importa la clase principal que contiene la lógica del sistema de biblioteca
from servicios.biblioteca_servicio import BibliotecaServicio

# Método que limpia la pantalla de la consola
def limpiar_pantalla():
    # Ejecuta el comando de limpieza dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

# Método que imprime un encabezado decorativo para las secciones del menú
def imprimir_encabezado(titulo: str):
    print("\n" + "=" * 55)
    print(f"  📚  {titulo}")
    print("=" * 55)

# Método que muestra el resultado de una operación (éxito o error)
def imprimir_resultado(exito: bool, mensaje: str):
    # Si la operación fue exitosa muestra un check, si no muestra una X
    icono = "✅" if exito else "❌"
    # Imprime el mensaje junto al icono correspondiente
    print(f"\n  {icono}  {mensaje}")

# Método que pausa la ejecución hasta que el usuario presione Enter
def pausar():
    input("\n  Presiona Enter para continuar...")

# Método que muestra una lista de libros en pantalla
def mostrar_lista_libros(libros: list, etiqueta: str = "Libros encontrados"):
    # Si la lista está vacía se informa al usuario
    if not libros:
        print(f"\n  ⚠️ No hay {etiqueta.lower()}📚.")
        return
    # Muestra la etiqueta y el número total de libros encontrados
    print(f"\n  {etiqueta} ({len(libros)}):\n")

    # Bucle que ecorre la lista de libros enumerándolos
    for i, libro in enumerate(libros, 1):
        print(f"  [{i}]")
        print(libro)
        print()

# Menú que gestiona las operaciones relacionadas con libros
def menu_libros(servicio: BibliotecaServicio):
    # Bucle infinito que mantiene activo el menú
    while True:
        imprimir_encabezado("GESTIÓN DE LIBROS")
        print("  1. Agregar libro")
        print("  2. Quitar libro")
        print("  3. Ver todos los libros")
        print("  4. Ver libros disponibles")
        print("  0. Volver al menú principal")
        print()

        # Solicita la opción al usuario
        opcion = input("  Selecciona una opción: ").strip()

        # Si el usuario quiere agregar un libro
        if opcion == "1":
            imprimir_encabezado("AGREGAR LIBRO")
            # Solicita los datos del libro
            titulo    = input("  Título    : ").strip()
            autor     = input("  Autor     : ").strip()
            categoria = input("  Categoría : ").strip()
            isbn      = input("  ISBN      : ").strip()
            # Llama al servicio para agregar el libro
            exito, msg = servicio.agregar_libro(titulo, autor, categoria, isbn)
            # Muestra el resultado
            imprimir_resultado(exito, msg)
            pausar()

        # Si el usuario quiere eliminar un libro
        elif opcion == "2":
            imprimir_encabezado("QUITAR LIBRO")
            isbn = input("  ISBN del libro a quitar: ").strip()
            exito, msg = servicio.quitar_libro(isbn)
            imprimir_resultado(exito, msg)
            pausar()

        # Mostrar todos los libros
        elif opcion == "3":
            imprimir_encabezado("TODOS LOS LIBROS")
            libros = servicio.listar_todos_los_libros()
            mostrar_lista_libros(libros, "Libros registrados en el sistema")
            pausar()

        # Mostrar libros disponibles
        elif opcion == "4":
            imprimir_encabezado("LIBROS DISPONIBLES")
            libros = servicio.listar_libros_disponibles()
            mostrar_lista_libros(libros, "Libros disponibles para préstamo")
            pausar()

        # Volver al menú principal
        elif opcion == "0":
            break

        # Si la opción no es válida
        else:
            print("\n  ⚠️  Opción no válida.")
            pausar()

# Menú para gestionar los usuarios registrados
def menu_usuarios(servicio: BibliotecaServicio):
    while True:
        imprimir_encabezado("GESTIÓN DE USUARIOS")
        print("  1. Registrar usuario")
        print("  2. Dar de baja usuario")
        print("  3. Ver todos los usuarios")
        print("  0. Volver al menú principal")
        print()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            imprimir_encabezado("REGISTRAR USUARIO")
            nombre     = input("  Nombre      : ").strip()
            id_usuario = input("  ID de usuario: ").strip()
            exito, msg = servicio.registrar_usuario(nombre, id_usuario)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "2":
            imprimir_encabezado("DAR DE BAJA USUARIO")
            id_usuario = input("  ID del usuario: ").strip()
            exito, msg = servicio.dar_baja_usuario(id_usuario)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "3":
            imprimir_encabezado("USUARIOS REGISTRADOS")
            usuarios = servicio.listar_usuarios()
            if not usuarios:
                print("\n  ⚠️  No hay usuarios registrados.")
            else:
                print(f"\n  Total: {len(usuarios)} usuario(s)\n")
                for u in usuarios:
                    print(u)
                    print()
            pausar()

        elif opcion == "0":
            break
        else:
            print("\n  ⚠️  Opción no válida.")
            pausar()

# Menú para gestionar los préstamos y devoluciones de los libros
def menu_prestamos(servicio: BibliotecaServicio):
    while True:
        imprimir_encabezado("PRÉSTAMOS Y DEVOLUCIONES")
        print("  1. Prestar libro")
        print("  2. Devolver libro")
        print("  3. Ver libros prestados a un usuario")
        print("  0. Volver al menú principal")
        print()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            imprimir_encabezado("PRESTAR LIBRO")
            isbn       = input("  ISBN del libro  : ").strip()
            id_usuario = input("  ID del usuario  : ").strip()
            exito, msg = servicio.prestar_libro(isbn, id_usuario)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "2":
            imprimir_encabezado("DEVOLVER LIBRO")
            isbn       = input("  ISBN del libro  : ").strip()
            id_usuario = input("  ID del usuario  : ").strip()
            exito, msg = servicio.devolver_libro(isbn, id_usuario)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "3":
            imprimir_encabezado("LIBROS PRESTADOS A USUARIO")
            id_usuario = input("  ID del usuario: ").strip()
            exito, resultado = servicio.listar_libros_prestados_a_usuario(id_usuario)
            if not exito:
                imprimir_resultado(False, str(resultado))
            else:
                mostrar_lista_libros(list(resultado), f"Libros prestados al usuario '{id_usuario}'")
            pausar()

        elif opcion == "0":
            break
        else:
            print("\n  ⚠️  Opción no válida.")
            pausar()

# Menú para gestionar las búsquedas de los libros
def menu_busquedas(servicio: BibliotecaServicio):
    while True:
        imprimir_encabezado("BÚSQUEDA EN CATÁLOGO")
        print("  1. Buscar por título")
        print("  2. Buscar por autor")
        print("  3. Buscar por categoría")
        print("  0. Volver al menú principal")
        print()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            termino = input("  Ingresa el título a buscar: ").strip()
            resultados = servicio.buscar_por_titulo(termino)
            mostrar_lista_libros(resultados, f"Resultados para título '{termino}'")
            pausar()

        elif opcion == "2":
            termino = input("  Ingresa el autor a buscar: ").strip()
            resultados = servicio.buscar_por_autor(termino)
            mostrar_lista_libros(resultados, f"Resultados para autor '{termino}'")
            pausar()

        elif opcion == "3":
            termino = input("  Ingresa la categoría a buscar: ").strip()
            resultados = servicio.buscar_por_categoria(termino)
            mostrar_lista_libros(resultados, f"Resultados para categoría '{termino}'")
            pausar()

        elif opcion == "0":
            break
        else:
            print("\n  ⚠️  Opción no válida.")
            pausar()

# Método para cargar datos por defecto o prueba
def cargar_datos_demo(servicio: BibliotecaServicio):
    servicio.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-84-376-0494-7")
    servicio.agregar_libro("El Aleph",              "Jorge Luis Borges",      "Cuentos", "978-84-206-5398-2")
    servicio.agregar_libro("1984",                  "George Orwell",          "Distopía", "978-0-452-28423-4")
    servicio.agregar_libro("Don Quijote",           "Miguel de Cervantes",    "Clásico", "978-84-670-5137-6")
    servicio.agregar_libro("La sombra del viento",  "Carlos Ruiz Zafón",      "Misterio", "978-84-08-04364-2")
    servicio.agregar_libro("Ficciones",             "Jorge Luis Borges",      "Cuentos", "978-84-206-5399-9")
    
    servicio.registrar_usuario("Ana García",   "USR001")
    servicio.registrar_usuario("Luis Martínez","USR002")
    servicio.registrar_usuario("María López",  "USR003")

    servicio.prestar_libro("978-84-376-0494-7", "USR001")
    servicio.prestar_libro("978-0-452-28423-4", "USR002")

    print("\n ✅ Datos de demostración cargados correctamente.")

# Función principal del sistema
def menu_principal():
    # Crea la instancia del servicio de biblioteca
    servicio = BibliotecaServicio()

    # Muestra el encabezado del sistema
    print("\n" + "=" * 55)
    print("  📚  SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
    print("=" * 55)

    # Pregunta al usuario si desea cargar datos de prueba
    print("\n  ¿Deseas cargar datos de demostración?")

    respuesta = input("  (s/n): ").strip().lower()

    # Si responde que sí se cargan libros y usuarios de ejemplo
    if respuesta == "s":
        cargar_datos_demo(servicio)
        pausar()

    # Bucle principal del programa
    while True:
        imprimir_encabezado("MENÚ PRINCIPAL")
        print(" 📚 1. Gestión de Libros")
        print(" 👤 2. Gestión de Usuarios")
        print(" 🔙 3. Préstamos y Devoluciones")
        print(" 🔎 4. Búsqueda en Catálogo")
        print(" 🚪 0. Salir")
        print()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            menu_libros(servicio)
        elif opcion == "2":
            menu_usuarios(servicio)
        elif opcion == "3":
            menu_prestamos(servicio)
        elif opcion == "4":
            menu_busquedas(servicio)
        elif opcion == "0":
            # Mensaje de despedida
            print("\n 👋 ¡Hasta luego! Gracias por usar el Sistema de Gestión de Biblioteca Digital 📚\n")
            break
        else:
            print("\n ⚠️ Opción no válida. Intenta de nuevo.")
            pausar()

# Punto de entrada del programa, que llama a la función main para iniciar el sistema de gestión de biblioteca digital
if __name__ == "__main__":
    menu_principal()