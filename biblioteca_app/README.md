# 📚 Sistema de Gestión de Biblioteca Digital 📄

Este proyecto consiste en un sistema de gestión de biblioteca digital desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y una arquitectura estructurada por capas.

El sistema permite administrar libros y usuarios mediante un menú interactivo en consola, aplicando correctamente las colecciones de Python y separando la lógica de negocio de la presentación.

---

## 🎯 Objetivos del Proyecto

### 💻 Desarrollar un sistema para gestionar una biblioteca digital aplicando:

- Encapsulamiento con atributos privados y propiedades (`@property`)
- Programación Orientada a Objetos (POO)
- Uso de colecciones: `tuple`, `list`, `dict`, `set`
- Separación por capas (modelos, servicios y archivo principal)
- Validaciones de datos en cada operación
- Manejo de errores con mensajes claros al usuario

---

## 🗂️ Estructura del Repositorio

```
biblioteca_app/
│
├── modelos/                    # Capa de datos: entidades del sistema
│   ├── __init__.py
│   ├── libro.py                 
│   └── usuario.py              
│
├── servicios/                  # Capa de lógica de negocio
│   ├── __init__.py
│   └── biblioteca_servicio.py  
│
├── main.py                     # Punto de entrada y menú interactivo
└── README.md                   # Documentación del proyecto
```

---

## 📦 Clases Principales

### Clase `Libro`

Representa un libro dentro del sistema.

**Atributos privados:**
- `_info` — tupla inmutable con `(título, autor)`
- `_categoria` — categoría o género del libro
- `_isbn` — identificador único del libro

**Métodos:**
- Constructor
- Propiedades de solo lectura (`titulo`, `autor`, `isbn`, `categoria`)
- `__str__` para visualización en consola

---

### Clase `Usuario`

Representa a un usuario registrado en la biblioteca.

**Atributos privados:**
- `_nombre` — nombre completo
- `_id_usuario` — identificador único
- `_libros_prestados` — lista de objetos `Libro` actualmente prestados

**Métodos:**
- Constructor
- Propiedades de solo lectura
- `_agregar_libro()` / `_quitar_libro()` — métodos protegidos gestionados desde el servicio
- `tiene_libro(isbn)` — verificación de préstamo activo

---

## ⚙️ Uso de Colecciones

Se utilizan cuatro tipos de colecciones con justificación técnica:

```python
# Tupla: título y autor son inmutables una vez definidos
self._info = (titulo, autor)

# Lista: los préstamos cambian con el tiempo (mutable y ordenada)
self._libros_prestados = []

# Diccionario: acceso O(1) por ISBN como clave única
self._libros_disponibles = {}

# Conjunto (set): garantiza IDs de usuario únicos, búsqueda en O(1)
self._ids_usuarios = set()
```

| Colección | Dónde se usa | Por qué |
|-----------|-------------|---------|
| `tuple` | `Libro._info` | Título y autor son datos inmutables |
| `list` | `Usuario._libros_prestados` | Colección ordenada y mutable |
| `dict` | `BibliotecaServicio._libros_disponibles` | Búsqueda directa por ISBN |
| `set` | `BibliotecaServicio._ids_usuarios` | Unicidad garantizada de IDs |

---

## 🧠 Funcionamiento General

El sistema funciona de la siguiente manera:

1. El usuario interactúa con un menú principal en consola desde `main.py`.
2. Cada operación es delegada completamente a `BibliotecaServicio`.
3. El servicio valida los datos y retorna una tupla `(bool, mensaje)` indicando éxito o error.
4. `main.py` solo presenta los resultados, sin contener lógica de negocio.

Las operaciones disponibles son:

- **Libros:** agregar, quitar, listar todos, listar disponibles
- **Usuarios:** registrar, dar de baja, listar todos
- **Préstamos:** prestar libro, devolver libro, listar préstamos de un usuario
- **Búsquedas:** por título, por autor, por categoría

---

## ⚠️ Validaciones Implementadas

El sistema controla los siguientes casos:

- ISBN duplicado al agregar un libro
- ID de usuario duplicado al registrar
- Intento de prestar un libro ya prestado
- Intento de devolver un libro que el usuario no tiene
- Dar de baja un usuario con préstamos pendientes
- Eliminar un libro que está actualmente prestado
- Búsqueda de usuario o libro inexistente

Cada validación retorna un mensaje descriptivo al usuario sin interrumpir la ejecución del programa.

---

## 🔔 Retroalimentación al Usuario

El menú informa al usuario sobre cada operación mediante iconos visuales:

- ✅ Operación realizada exitosamente
- ❌ Error detectado con descripción del problema
- ⚠️ Advertencia o lista vacía

---

## 🧪 Pruebas Realizadas

Se realizaron pruebas en los siguientes escenarios:

- Registro de usuarios e intento de duplicar IDs
- Agregar libros e intentar duplicar ISBN
- Préstamo de un libro ya prestado
- Devolución de un libro no perteneciente al usuario
- Búsquedas con texto parcial (sin distinguir mayúsculas)
- Dar de baja usuario con y sin libros pendientes
- Carga de datos de demostración al inicio del programa

Los resultados confirmaron que el sistema mantiene consistencia en todas las operaciones.

---

## 🚀 Cómo Ejecutar el Programa

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   ```
2. **Abrir en IDE:** PyCharm o Visual Studio Code.
3. **Ejecutar:**
   ```bash
   python main.py
   ```
4. Al iniciar, selecciona **"s"** para cargar datos de demostración y probar el sistema de inmediato.

---

## 🏁 Conclusión

Este proyecto permitió aplicar de manera práctica los conceptos de Programación Orientada a Objetos en Python, integrando colecciones adecuadas para cada necesidad del sistema.

La arquitectura por capas garantiza una separación clara entre los modelos de datos, la lógica de negocio y la interfaz de usuario, haciendo el código más organizado, mantenible y escalable.

El sistema demuestra la correcta aplicación de:

- POO y encapsulamiento
- Colecciones (`tuple`, `list`, `dict`, `set`)
- Arquitectura por capas (modelos / servicios / main)
- Validaciones y manejo de errores
- Buenas prácticas de organización y documentación
