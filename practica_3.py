"""
3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario.
"""
var_1 = str(input("Ingrese su nombre: "))
var_2 = str(input("Ingrese sus apellidos: "))
var_3 = int(input("Ingrese su edad: "))
var_4 = int(input("Ingrese su DNI: "))
diccionario = { "nombre": var_1 , "apellidos": var_2 ,"edad": var_3, "dni": var_4 }

values = diccionario.values()
print(f"Los values de mi diccionario son: {values}")

diccionario["profesion"] = "Ingenieria En Energia"
print(f"Los valores actualizados de mi diccionario son: {diccionario}")

del diccionario["dni"]
print(f"Los valores actualizados de mi diccionario, eliminando el key 'dni' son los siguientes: {diccionario}")