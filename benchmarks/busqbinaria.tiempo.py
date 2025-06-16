import timeit
import random

def busqueda_binaria(lista, objetivo):
    izquierda = 0  # inicializa el índice izquierdo al comienzo de la lista
    derecha = len(lista) - 1  # inicializa el índice derecho al final de la lista

    while izquierda <= derecha:  # mientras el rango de búsqueda sea válido
        medio = (izquierda + derecha) // 2  # calcula el índice medio
        if lista[medio] == objetivo:
            return medio  # si encuentra el objetivo, devuelve su índice
        if lista[medio] < objetivo:
            izquierda = medio + 1  # si el objetivo es mayor, descarta la mitad izquierda
        else:
            derecha = medio - 1  # si el objetivo es menor, descarta la mitad derecha
    return -1  # si no encuentra, devuelve -1

# generar listas de prueba
lista_ordenada = list(range(1000))  # lista ordenada para búsqueda binaria

# definir funciones para ejecutar las pruebas
def ejecutar_mejor_caso():
    busqueda_binaria(lista_ordenada, lista_ordenada[len(lista_ordenada) // 2])  # objetivo está en el medio

def ejecutar_peor_caso():
    busqueda_binaria(lista_ordenada, -1)  # objetivo no está en la lista

# medir tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=1000)  # mejor caso O(1)
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=0000)  # peor caso O(log n)

print(f"Búsqueda Binaria - Mejor caso (O(1)): {tiempo_mejor:.5f} segundos")
print(f"Búsqueda Binaria - Peor caso (O(log n)): {tiempo_peor:.5f} segundos")