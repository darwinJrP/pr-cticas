import funciones


def main():
    nombre_archivo = "notas.txt"
    tamano_lista = int(input("Ingrese el tamaño de la lista: "))

    lista_numeros = funciones.crear_lista_tamano_aleatorio(tamano_lista)
    funciones.escribir_lista_en_archivo(lista_numeros, nombre_archivo)

    # RAICES CUADRADAS
    funciones.calcular_raiz_cuadrada(lista_numeros, nombre_archivo)


if __name__ == "__main__":
    main()
