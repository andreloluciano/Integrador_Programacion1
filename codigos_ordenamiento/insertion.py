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

# generamos una lista aleatoria 
lista = [random.randint(1, 100) for _ in range(10)]
lista_original = lista[:]  

print(f"Lista original: {lista_original}")  
print(f"Lista ordenada: {insertion_sort(lista)}")  





# for i in range(1, len(lista)):  # recorre desde el segundo elemento hasta el final
#     clave = lista[i]  # valor actual que vamos a insertar en la parte ordenada
#     j = i - 1  # empezamos a comparar hacia atrás

#     while j >= 0 and clave < lista[j]:  # mientras la clave sea menor, desplazamos
#         lista[j + 1] = lista[j]  # movemos el valor hacia adelante
#         j -= 1  # nos movemos una posición hacia atrás

#     lista[j + 1] = clave  # colocamos la clave en su lugar correcto

# print(f"Lista ordenada: {lista}")

# codigo colab
# def insertion_sort(arr):
#   for i in range(1, len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >=0 and key < arr[j] :
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key
