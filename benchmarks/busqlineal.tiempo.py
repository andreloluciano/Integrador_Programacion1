import timeit
import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):  # recorre la lista completa
        if lista[i] == objetivo:
            return i  # devuelve el índice donde se encontró
    return -1  # si no se encuentra, devuelve -1

# generamos listas de prueba
lista_ordenada = list(range(10000))  # lista ordenada para prueba

# definimos funciones para ejecutar las pruebas
def ejecutar_mejor_caso():
    busqueda_lineal(lista_ordenada, lista_ordenada[0])  # objetivo está en la primera posición

def ejecutar_peor_caso():
    busqueda_lineal(lista_ordenada, -1)  # objetivo no está en la lista

# Medir tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=10000)  # mejor caso O(1)
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=10000)  # peor caso O(n)

print(f"Búsqueda Lineal - Mejor caso (O(1)): {tiempo_mejor:.5f} segundos")
print(f"Búsqueda Lineal - Peor caso (O(n)): {tiempo_peor:.5f} segundos")