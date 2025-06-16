import timeit
import random
import sys
sys.setrecursionlimit(5000)  # como quickSort es n², aumentamos el limite de recursion

def quicksort(arr):
    if len(arr) <= 1:  # caso base: una lista de 0 o 1 elemento ya está ordenada
        return arr
    else:
        pivot = arr[0]  # elige el primer elemento como pivote
        less = [x for x in arr[1:] if x <= pivot]  # elementos menores o iguales al pivote
        greater = [x for x in arr[1:] if x > pivot]  # elementos mayores al pivote      
        return quicksort(less) + [pivot] + quicksort(greater)  # aplica recursión y combina resultados

# generamos listas de prueba
lista_mejor_caso = list(range(3000))  # lista ordenada (mejor caso)
lista_peor_caso = list(range(3000, 0, -1))  # lista en orden inverso (peor caso)

# definimos funciones para ejecutar las pruebas
def ejecutar_mejor_caso():
    quicksort(lista_mejor_caso[:])

def ejecutar_peor_caso():
    quicksort(lista_peor_caso[:])

# Medir tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=2)  # necesario para que timeit ejecute funciones externas
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=2)

print(f"QuickSort - Mejor caso (O(n log n)): {tiempo_mejor:.5f} segundos")
print(f"QuickSort - Peor caso (O(n²)): {tiempo_peor:.5f} segundos")