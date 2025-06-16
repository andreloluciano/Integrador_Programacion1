import timeit
import random

def insertion_sort(lista):  # definimos la función de ordenamiento por inserción
    for i in range(1, len(lista)):  # recorremos desde el segundo elemento hasta el final
        clave = lista[i]  # guardamos el valor actual que vamos a insertar en la parte ordenada
        j = i - 1  # empezamos a comparar desde la posición anterior
        
        while j >= 0 and clave < lista[j]:  # mientras haya elementos mayores, desplazamos
            lista[j + 1] = lista[j]  # movemos los valores hacia adelante
            j -= 1  # nos movemos una posición hacia atrás
        
        lista[j + 1] = clave  # insertamos la clave en su posición correcta
    return lista  # devolvemos la lista ordenada

# generamos listas de prueba
lista_mejor_caso = list(range(5000))  # lista ordenada (mejor caso)
lista_peor_caso = list(range(5000, 0, -1))  # lista en orden inverso (peor caso)

# definimos funciones para ejecutar las pruebas
def ejecutar_mejor_caso():
    insertion_sort(lista_mejor_caso[:])

def ejecutar_peor_caso():
    insertion_sort(lista_peor_caso[:])

# medimos tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=2)  # para que timeit ejecute funciones externas
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=2)

print(f"Insertion Sort - Mejor caso (O(n)): {tiempo_mejor:.5f} segundos")
print(f"Insertion Sort - Peor caso (O(n²)): {tiempo_peor:.5f} segundos")