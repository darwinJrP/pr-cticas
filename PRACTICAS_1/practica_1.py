
nombre = str(input("Ingrese su nombre: "))

edad = int(input("Ingrese su edad: "))

print(f"Los tipos de datos ingresados son: {type(nombre)} {type(edad)}")

trabajador_1 = str(input("Ingrese el nombre para el trabajador_1: "))
edad_1 = int(input("Ingrese la edad para el trabajador_1: "))

trabajador_2 = str(input("Ingrese el nombre para el trabajador_2: "))
edad_2 = int(input("Ingrese la edad para el trabajador_2: "))


lista = []

lista.append(trabajador_1)
lista.append(edad_1)
lista.append(trabajador_2)
lista.append(edad_2)

print(f"Los elementos de mi lista son: {lista}")

suma_edades = lista[1] + lista[3]
print(f"La suma de las edades de trabajador_1 y trabajador_2 es: {suma_edades}")