# funciones.py
import random
import math


def crear_lista_tamano_aleatorio(tamano):
    return [random.randint(1, 666) for _ in range(tamano)]


def escribir_lista_en_archivo(lista, nombre_archivo):
    file = open(nombre_archivo, 'w')
    for numero in lista:
        file.write(str(numero) + '\n')
    file.close()


def calcular_raiz_cuadrada(lista, nombre_archivo):
    file = open(nombre_archivo, 'a')
    for numero in lista:
        raiz = math.sqrt(numero)
        file.write(str(raiz) + '\n')
    file.close()