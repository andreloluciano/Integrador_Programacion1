# Busquedas

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i # devuelve el indice donde se encontro
    return -1 #si no se encuentra, devuelve -1

def busqueda_binaria(lista, objetivo):
    izquierda = 0 # incializa el indice izquierdo al comienzo de la lista
    derecha = len(lista) - 1 # inicializa el indice derecho al final de la lista

    while izquierda <= derecha: # mientras el rango de busqueda sea valido
        medio = (izquierda + derecha) // 2 # calcula el indice medio
        if lista[medio] == objetivo:
            return medio  # si encuentra el objetivo, devuelve su indice
        if lista[medio] < objetivo:
            izquierda = medio + 1  # si el objetivo es mayor, descarta la mitad izquierda
        else:
            derecha = medio - 1  # si el obj es menor, descarta la mitad derecha
    return -1  # si no encuentra, devuelve -1

# Ordenamientos

def bubble_sort(lista):
    n = len(lista)  # cantidad de valores en la lista

    for i in range(n): # recorre la lista 
        for j in range(0, n - i - 1): # en cada iteracion, compara pares de valores adyacentes
            if lista[j] > lista[j + 1]: # si el valor actual es mayor que el siguiente, lo intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # esto asegura que el valor mas alto "suba" al final del array

def selection_sort(lista):
    n = len(lista) # guardamos la cantidad de valores
    for i in range(n - 1):  # itera hasta el anteultimo elemento
        min_indice = i # guarda el valor actual como el minimo 
        for j in range(i + 1, n): # el bucle interno busca el menor valor restante
            if lista[j] < lista[min_indice]:  
                min_indice = j  # reemplaza el valor minimo si es mas chico
        lista[i], lista[min_indice] = lista[min_indice], lista[i] # intercambia el valor mínimo encontrado con la posición actual 
    return lista  # devuelve la lista ordenada

def insertion_sort(lista):  # definimos la función de ordenamiento por inserción
    for i in range(1, len(lista)):  # recorremos desde el segundo elemento hasta el final
        clave = lista[i]  # guardamos el valor actual que vamos a insertar en la parte ordenada
        j = i - 1  # empezamos a comparar desde la posición anterior
        
        while j >= 0 and clave < lista[j]:  # mientras haya elementos mayores, desplazamos
            lista[j + 1] = lista[j]  # movemos los valores hacia adelante
            j -= 1  # nos movemos una posición hacia atrás
        
        lista[j + 1] = clave  # insertamos la clave en su posición correcta
    return lista  # devolvemos la lista ordenada

def quicksort(arr):
    if len(arr) <= 1:  # caso base una lista de 0 o 1 elemento ya está ordenada
        return arr
    else:
        pivot = arr[0]  # elige el primer elemento como pivote
        less = [x for x in arr[1:] if x <= pivot] # crea una lista con todos los elementos menores o iguales al pivote
        greater = [x for x in arr[1:] if x > pivot] # creamos una lista con todos los elementos mayores al pivote      
        return quicksort(less) + [pivot] + quicksort(greater)  # aplica quicksort recursivamente y combinamos los resultados