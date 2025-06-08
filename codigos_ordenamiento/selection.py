import random

def selection_sort(lista):
    n = len(lista) # guardamos la cantidad de valores
    for i in range(n - 1):  # itera hasta el anteultimo elemento
        min_indice = i # guarda el valor actual como el minimo 
        for j in range(i + 1, n): # el bucle interno busca el menor valor restante
            if lista[j] < lista[min_indice]:  
                min_indice = j  # reemplaza el valor minimo si es mas chico
        lista[i], lista[min_indice] = lista[min_indice], lista[i] # intercambia el valor mínimo encontrado con la posición actual 
    return lista  # devuelve la lista ordenada

# Generamos la lista y llamamos a la función
lista = [random.randint(1, 100) for _ in range(10)]
lista_original = lista

print(f"Lista original: {lista_original}")
print(f"Lista ordenada: {selection_sort(lista)}")



# n = len(lista)  # guardamos la cantidad de valores

# for i in range(n - 1):  # itera hasta el penúltimo elemento
#     min_indice = i  # guarda valor actual como el mínimo
#     for j in range(i + 1, n):  # el bucle interno busca el menor valor restante
#         if lista[j] < lista[min_indice]:
#             min_indice = j  # reemplaza el valor mínimo si es más chico

#     # intercambia el valor mínimo encontrado con la posición actual
#     lista[i], lista[min_indice] = lista[min_indice], lista[i]

# print(f"Lista ordenada: {lista}")


# codigo de colab
# def insertion_sort(arr):
#     for i in range(1, len(arr)): # empezamos desde el segundo valor
#         key = arr[i] # guarda el valor actual ordenado, toma la posicion i guardandolo en key para ir comparando
#         j = i - 1 # define el indice del elemento anterior al actual, para comparar hacia atras
#         while j >= 0 and key < arr[j]: # bucle que compara hacia atras en la parte ya ordenada
#             arr[j + 1] = arr[j] # mueve a la derecha cualquier valor mayor a key
#             j -= 1 # compara valores anteriores
#             arr[j + 1] = key # inserta el valor en la posicion correcta



