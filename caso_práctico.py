import sys # Para sys.exit()
import time # Importar el módulo time para medir el tiempo de ejecución

def mostrar_contenido(contenido, titulo_seccion="Resultados"):
    """Función auxiliar para imprimir la lista de contenido de forma legible."""
    print(f"\n--- {titulo_seccion} ---")
    if not contenido:
        print("No hay contenido para mostrar.")
        return
    for item in contenido:
        disponible_4k_str = "Sí" if item['disponible_4k'] else "No"
        print(f"ID: {item['id']}, Título: {item['titulo']}, Género: {item['genero']}, "
              f"Año: {item['anio_lanzamiento']}, Calificación: {item['calificacion']:.1f}, 4K: {disponible_4k_str}")
    print("-" * 100)

# --- Catálogo de Streaming Inicial ---
catalogo_streaming = [
    {"id": "MOV005", "titulo": "El Viaje de Chihiro", "genero": "Animación", "anio_lanzamiento": 2001, "calificacion": 9.5, "disponible_4k": False},
    {"id": "SER002", "titulo": "Stranger Things", "genero": "Ciencia Ficción", "anio_lanzamiento": 2016, "calificacion": 8.8, "disponible_4k": True},
    {"id": "MOV001", "titulo": "Pulp Fiction", "genero": "Crimen", "anio_lanzamiento": 1994, "calificacion": 8.9, "disponible_4k": False},
    {"id": "SER007", "titulo": "The Crown", "genero": "Drama", "anio_lanzamiento": 2016, "calificacion": 8.7, "disponible_4k": True},
    {"id": "MOV003", "titulo": "Interestelar", "genero": "Ciencia Ficción", "anio_lanzamiento": 2014, "calificacion": 8.6, "disponible_4k": True},
    {"id": "SER006", "titulo": "Breaking Bad", "genero": "Drama", "anio_lanzamiento": 2008, "calificacion": 9.5, "disponible_4k": True},
    {"id": "MOV004", "titulo": "Forrest Gump", "genero": "Drama", "anio_lanzamiento": 1994, "calificacion": 8.8, "disponible_4k": False},
    {"id": "SER008", "titulo": "Arcane", "genero": "Animación", "anio_lanzamiento": 2021, "calificacion": 9.1, "disponible_4k": True},
]

# --- Funciones de Búsqueda ---

def busqueda_lineal_por_titulo(catalogo, palabra_clave):
    """Busca contenido por una palabra clave en el título (insensible a mayúsculas/minúsculas) usando búsqueda lineal."""
    resultados = []
    palabra_clave_lower = palabra_clave.lower()
    for item in catalogo:
        if palabra_clave_lower in item['titulo'].lower():
            resultados.append(item)
    return resultados

def busqueda_binaria_por_id(catalogo_ordenado_por_id, id_buscado):
    """
    Busca un elemento de contenido por su ID único usando búsqueda binaria.
    Requiere que el catálogo esté ordenado por ID.
    """
    izquierda, derecha = 0, len(catalogo_ordenado_por_id) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        item_medio = catalogo_ordenado_por_id[medio]
        if item_medio['id'] == id_buscado:
            return item_medio
        elif id_buscado < item_medio['id']:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return None

def busqueda_lineal_por_genero(catalogo, genero_buscado):
    """Filtra el contenido por un género específico (insensible a mayúsculas/minúsculas) usando búsqueda lineal."""
    resultados = []
    genero_buscado_lower = genero_buscado.lower()
    for item in catalogo:
        if item['genero'].lower() == genero_buscado_lower:
            resultados.append(item)
    return resultados

def busqueda_lineal_contenido_4k(catalogo):
    """Encuentra todo el contenido disponible en 4K usando búsqueda lineal."""
    resultados = []
    for item in catalogo:
        if item['disponible_4k']:
            resultados.append(item)
    return resultados

# --- Funciones de Ordenamiento ---

# Helper para Quick Sort
def partition(arr, low, high, key_func, reverse):
    pivot = key_func(arr[high])
    i = low - 1
    for j in range(low, high):
        current_value = key_func(arr[j])
        if (reverse and current_value >= pivot) or (not reverse and current_value <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high, key_func, reverse):
    if low < high:
        pi = partition(arr, low, high, key_func, reverse)
        quick_sort_recursive(arr, low, pi - 1, key_func, reverse)
        quick_sort_recursive(arr, pi + 1, high, key_func, reverse)

def quick_sort_por_calificacion(catalogo):
    """Ordena el contenido por calificación (de mayor a menor) usando Quick Sort."""
    lista_copia = catalogo[:]
    quick_sort_recursive(lista_copia, 0, len(lista_copia) - 1, lambda item: item['calificacion'], True)
    return lista_copia

def selection_sort_por_anio(catalogo):
    """Ordena el contenido por año de lanzamiento (del más reciente al más antiguo) usando Selection Sort."""
    n = len(catalogo)
    lista_copia = catalogo[:]
    for i in range(n):
        indice_max = i
        for j in range(i + 1, n):
            if lista_copia[j]['anio_lanzamiento'] > lista_copia[indice_max]['anio_lanzamiento']:
                indice_max = j
        lista_copia[i], lista_copia[indice_max] = lista_copia[indice_max], lista_copia[i]
    return lista_copia

def insertion_sort_por_titulo(catalogo):
    """Ordena el contenido alfabéticamente por título usando Insertion Sort."""
    n = len(catalogo)
    lista_copia = catalogo[:]
    for i in range(1, n):
        clave = lista_copia[i]
        j = i - 1
        while j >= 0 and clave['titulo'].lower() < lista_copia[j]['titulo'].lower():
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = clave
    return lista_copia

# --- Función auxiliar para medir el tiempo ---
def medir_tiempo(func, *args, **kwargs):
    start_time = time.time()
    resultados = func(*args, **kwargs)
    end_time = time.time()
    tiempo_ejecucion_ms = (end_time - start_time) * 1000 # Convertir a milisegundos
    return resultados, tiempo_ejecucion_ms

# --- Funciones para la Interfaz Interactiva ---

def ejecutar_busqueda():
    print("\n--- Opciones de Búsqueda ---")
    print("1. Buscar por Título (Búsqueda Lineal)")
    print("2. Buscar por ID (Búsqueda Binaria)")
    print("3. Buscar por Género (Búsqueda Lineal)")
    print("4. Buscar Contenido en 4K (Búsqueda Lineal)")
    opcion_busqueda = input("Elige una opción de búsqueda: ")

    if opcion_busqueda == '1':
        palabra_clave = input("Ingresa la palabra clave para el título: ")
        resultados, tiempo = medir_tiempo(busqueda_lineal_por_titulo, catalogo_streaming, palabra_clave)
        mostrar_contenido(resultados, f"Resultados de búsqueda por título: '{palabra_clave}'")
        print(f"Tiempo de ejecución de Búsqueda Lineal por Título: {tiempo:.4f} ms") # Imprimir tiempo

    elif opcion_busqueda == '2':
        # Para la búsqueda binaria, la lista debe estar ordenada por ID.
        # Creamos una copia ordenada temporalmente para esta operación.
        catalogo_ordenado_por_id_para_busqueda = sorted(catalogo_streaming, key=lambda item: item['id'])
        id_buscado = input("Ingresa el ID del contenido a buscar: ")
        
        # Medir el tiempo de la búsqueda binaria
        resultado, tiempo = medir_tiempo(busqueda_binaria_por_id, catalogo_ordenado_por_id_para_busqueda, id_buscado)
        
        if resultado:
            mostrar_contenido([resultado], f"Contenido encontrado por ID: '{id_buscado}'")
        else:
            print(f"Contenido con ID '{id_buscado}' no encontrado.")
        print(f"Tiempo de ejecución de Búsqueda Binaria por ID: {tiempo:.4f} ms") # Imprimir tiempo

    elif opcion_busqueda == '3':
        genero_buscado = input("Ingresa el género a buscar: ")
        resultados, tiempo = medir_tiempo(busqueda_lineal_por_genero, catalogo_streaming, genero_buscado)
        mostrar_contenido(resultados, f"Resultados de búsqueda por género: '{genero_buscado}'")
        print(f"Tiempo de ejecución de Búsqueda Lineal por Género: {tiempo:.4f} ms") # Imprimir tiempo

    elif opcion_busqueda == '4':
        resultados, tiempo = medir_tiempo(busqueda_lineal_contenido_4k, catalogo_streaming)
        mostrar_contenido(resultados, "Contenido disponible en 4K")
        print(f"Tiempo de ejecución de Búsqueda Lineal 4K: {tiempo:.4f} ms") # Imprimir tiempo
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

def ejecutar_ordenamiento():
    print("\n--- Opciones de Ordenamiento ---")
    print("1. Ordenar por Calificación (Quick Sort)")
    print("2. Ordenar por Año de Lanzamiento (Selection Sort)")
    print("3. Ordenar por Título (Insertion Sort)")
    opcion_ordenamiento = input("Elige una opción de ordenamiento: ")

    if opcion_ordenamiento == '1':
        lista_ordenada, tiempo = medir_tiempo(quick_sort_por_calificacion, catalogo_streaming)
        mostrar_contenido(lista_ordenada, "Catálogo ordenado por Calificación (Quick Sort)")
        print(f"Tiempo de ejecución de Quick Sort por Calificación: {tiempo:.4f} ms") # Imprimir tiempo

    elif opcion_ordenamiento == '2':
        lista_ordenada, tiempo = medir_tiempo(selection_sort_por_anio, catalogo_streaming)
        mostrar_contenido(lista_ordenada, "Catálogo ordenado por Año de Lanzamiento (Selection Sort)")
        print(f"Tiempo de ejecución de Selection Sort por Año: {tiempo:.4f} ms") # Imprimir tiempo

    elif opcion_ordenamiento == '3':
        lista_ordenada, tiempo = medir_tiempo(insertion_sort_por_titulo, catalogo_streaming)
        mostrar_contenido(lista_ordenada, "Catálogo ordenado por Título (Insertion Sort)")
        print(f"Tiempo de ejecución de Insertion Sort por Título: {tiempo:.4f} ms") # Imprimir tiempo
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

def menu_principal():
    while True:
        print("\n===== Menú Principal del Catálogo de Streaming =====")
        print("1. Mostrar Catálogo Completo")
        print("2. Realizar una Búsqueda")
        print("3. Realizar un Ordenamiento")
        print("4. Salir")

        eleccion = input("Ingresa tu elección: ")

        if eleccion == '1':
            mostrar_contenido(catalogo_streaming, "Catálogo Completo")
        elif eleccion == '2':
            ejecutar_busqueda()
        elif eleccion == '3':
            ejecutar_ordenamiento()
        elif eleccion == '4':
            print("Saliendo del programa. ¡Gracias por usar el sistema!")
            sys.exit() # Sale del programa
        else:
            print("Elección no válida. Por favor, ingresa un número entre 1 y 4.")

# Iniciar la aplicación interactiva
if __name__ == "__main__":
    menu_principal()