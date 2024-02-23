import final_1_funciones

if __name__ == "__main__":
    lista_aleatoria = final_1_funciones.generar_lista_aleatoria()
    lista_sin_repetidos = final_1_funciones.eliminar_repetidos(lista_aleatoria)
    lista_ascendente, lista_descendente = \
        final_1_funciones.ordenar_lista(lista_sin_repetidos)
    final_1_funciones.mayor_numero_par(lista_sin_repetidos)
