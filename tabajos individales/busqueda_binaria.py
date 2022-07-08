import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        #range(len(lista))-> 0,1,2,3,4,5,6,7,........, len(lista)-1
        if lista [i] == objetivo:
            return i
    return -1 

def busqueda_binaria(lista, objetivo, limite_inferior = None, limite_superior = None):
    if limite_inferior is None:
        limite_inferior = 0 #inicio de la lista.
    if limite_superior is None:
        limite_superior = len(lista)-1 #Fin de la lista.

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_superior + limite_inferior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)

if __name__=='__main__':
    #creamos una lista ordenada con 100000 numeros aleatoreos.
    tamaño = 100000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista = sorted(list(conjunto_inicial))#sorted ordena la lisrta en orden acendente

    #medir tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista:
        busqueda_binaria(lista, objetivo)
    fin = time.time()
    print(f"tiempoi de busqueda binaria: {fin - inicio} segundos.")

    #medir tiempo de busqueda ingenua.
    inicio = time.time()
    for objetivo in lista:
        busqueda_ingenua(lista, objetivo)
    fin = time.time()
    print(f"tiempo de busqueda ingenua: {fin - inicio} segundos.")
    
