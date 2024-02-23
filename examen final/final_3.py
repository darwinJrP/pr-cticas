import datetime


def calcular_tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = datetime.datetime.now()
        resultado = func(*args, **kwargs)
        fin = datetime.datetime.now()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución de {func.__name__}: {tiempo_ejecucion.total_seconds()} segundos")
        return resultado
    return wrapper


@calcular_tiempo_ejecucion
def multiplicar_numeros(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


# EJEMPLO DE USO
print(multiplicar_numeros(6, 25, 111))
print(multiplicar_numeros(7, 7, 7, 7))
print(multiplicar_numeros(4, 3, 2, 1, 666))
