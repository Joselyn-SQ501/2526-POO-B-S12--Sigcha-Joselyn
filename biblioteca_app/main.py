import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from servicios.biblioteca_servicio import BibliotecaServicio

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_encabezado(titulo: str):
    print("\n" + "=" * 55)
    print(f"  📚  {titulo}")
    print("=" * 55)


def imprimir_resultado(exito: bool, mensaje: str):
    icono = "✅" if exito else "❌"
    print(f"\n  {icono}  {mensaje}")


def pausar():
    input("\n  Presiona Enter para continuar...")


def mostrar_lista_libros(libros: list, etiqueta: str = "Libros encontrados"):
    if not libros:
        print(f"\n  ⚠️  No hay {etiqueta.lower()}.")
        return
    print(f"\n  {etiqueta} ({len(libros)}):\n")
    for i, libro in enumerate(libros, 1):
        print(f"  [{i}]")
        print(libro)
        print()

def menu_libros(servicio: BibliotecaServicio):
    while True:
        imprimir_encabezado("GESTIÓN DE LIBROS")
        print("  1. Agregar libro")
        print("  2. Quitar libro")
        print("  3. Ver todos los libros")
        print("  4. Ver libros disponibles")
        print("  0. Volver al menú principal")
        print()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            imprimir_encabezado("AGREGAR LIBRO")
            titulo    = input("  Título    : ").strip()
            autor     = input("  Autor     : ").strip()
            categoria = input("  Categoría : ").strip()
            isbn      = input("  ISBN      : ").strip()
            exito, msg = servicio.agregar_libro(titulo, autor, categoria, isbn)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "2":
            imprimir_encabezado("QUITAR LIBRO")
            isbn = input("  ISBN del libro a quitar: ").strip()
            exito, msg = servicio.quitar_libro(isbn)
            imprimir_resultado(exito, msg)
            pausar()

        elif opcion == "3":
            imprimir_encabezado("TODOS LOS LIBROS")
            libros = servicio.listar_todos_los_libros()
            mostrar_lista_libros(libros, "Libros registrados en el sistema")
            pausar()

        elif opcion == "4":
            imprimir_encabezado("LIBROS DISPONIBLES")
            libros = servicio.listar_libros_disponibles()
            mostrar_lista_libros(libros, "Libros disponibles para préstamo")
            pausar()

        elif opcion == "0":
            break
        else:
            print("\n  ⚠️  Opción no válida.")
            pausar()


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

    print("\n  ✅  Datos de demostración cargados correctamente.")

def menu_principal():
    servicio = BibliotecaServicio()

    print("\n" + "=" * 55)
    print("  📚  SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
    print("  Desarrollado con arquitectura por capas (POO)")
    print("=" * 55)
    print("\n  ¿Deseas cargar datos de demostración?")
    respuesta = input("  (s/n): ").strip().lower()
    if respuesta == "s":
        cargar_datos_demo(servicio)
        pausar()

    while True:
        imprimir_encabezado("MENÚ PRINCIPAL")
        print("  1. Gestión de Libros")
        print("  2. Gestión de Usuarios")
        print("  3. Préstamos y Devoluciones")
        print("  4. Búsqueda en Catálogo")
        print("  0. Salir")
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
            print("\n  👋  ¡Hasta luego!\n")
            break
        else:
            print("\n  ⚠️  Opción no válida. Intenta de nuevo.")
            pausar()

if __name__ == "__main__":
    menu_principal()