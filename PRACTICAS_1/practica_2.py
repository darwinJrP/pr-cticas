"""
2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas.
"""
lista = [] #PRIMERO CREÉ UNA LISTA VACÍA PARA LUEGO AGREGARLE LOS VALORES ALEATORIOS CON EL FOR Y APPEND

for e in range (1,11):
    lista.append(float(input(f"Ingrese el valor #{e} para la lista: ")))

print(f"Los valores de mi lista son: {lista}")


lista_cubos = []

for i in lista:
    lista_cubos.append(pow(i,3)) #UTILIZANDO pow en lugar de **

print(f"Los valores de los elementos de mi lista elevados al cubo son: {lista_cubos}")

lista_cuadrados = []

for k in lista:
    lista_cuadrados.append(pow(i,2))

print(f"Los valores de los elementos de mi lista elevados al cuadrado son: {lista_cuadrados}")

suma_listas = lista_cubos + lista_cuadrados
print(f"La suma de los elementos de lista_cubos y lista_cuadrados son: {suma_listas}")

suma_listas.reverse()
print(f"El inverso es: {suma_listas}")

