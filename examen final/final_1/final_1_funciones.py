import random


def generar_lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista aleatoria generada:", lista)
    return lista


def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print("Lista sin números repetidos:", lista_sin_repetidos)
    return lista_sin_repetidos


def ordenar_lista(lista):
    lista_ascendente = sorted(lista)
    lista_descendente = sorted(lista, reverse=True)
    print("Lista ordenada de menor a mayor:", lista_ascendente)
    print("Lista ordenada de mayor a menor:", lista_descendente)
    return lista_ascendente, lista_descendente


def mayor_numero_par(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    if numeros_pares:
        mayor_par = max(numeros_pares)
        print("Mayor número par de la lista:", mayor_par)
        return mayor_par
    else:
        print("No hay números pares en la lista.")
        return None
