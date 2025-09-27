#ejercicio 1

notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)
print("\nLista de notas:")
for n in notas:
    print(n, end=" ")
print()  
suma = 0
for n in notas:
    suma += n
promedio = suma / len(notas)
print(f"\nPromedio de las notas: {promedio:.2f}")
nota_max = notas[0]
nota_min = notas[0]
for n in notas:
    if n > nota_max:
        nota_max = n
    if n < nota_min:
        nota_min = n
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

#ejercicio 2

productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for p in productos_ordenados:
    print(p)
producto_eliminar = input("\nIngrese el producto que desea eliminar: ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"\nProducto '{producto_eliminar}' eliminado.")
else:
    print(f"\nProducto '{producto_eliminar}' no se encontró en la lista.")
print("\nLista actualizada de productos:")
for p in productos:
    print(p)

#ejercicio 3

import random
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))
print("Lista generada:")
for n in numeros:
    print(n, end=" ")
print("\n")  
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Lista de números pares:")
for p in pares:
    print(p, end=" ")
print(f"\nCantidad de pares: {len(pares)}\n")
print("Lista de números impares:")
for i in impares:
    print(i, end=" ")
print(f"\nCantidad de impares: {len(impares)}")

#ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetidos = list(set(datos))
print("Lista original:")
for elemento in datos:
    print(elemento, end=" ") 
print("\n" + "-"*30) 
print("Nueva lista sin elementos repetidos:")
for elemento_unico in lista_sin_repetidos:
    print(elemento_unico, end=" ")
print() 

#ejercicio 5

estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    estudiantes.append(nombre)
print("\nLista de estudiantes:")
for e in estudiantes:
    print(e)
while True:
    opcion = input("\nDesea agregar o eliminar un estudiante? (agregar/eliminar/terminar): ").lower()
    if opcion == "agregar":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo)
        print(f"{nuevo} agregado.")  
    elif opcion == "eliminar":
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
            print(f"{eliminar} eliminado.")
        else:
            print(f"{eliminar} no se encontró en la lista.")
    elif opcion == "terminar":
        break
    else:
        print("Opción no válida. Ingrese 'agregar', 'eliminar' o 'terminar'.")
print("\nLista final de estudiantes:")
for e in estudiantes:
    print(e)

#ejercicio 6

numeros = [9, 25, 32, 11, 30, 5, 6]
print("Lista original:")
i = 0
while i < len(numeros):
    print(numeros[i], end=" ")
    i += 1
print("\n")
ultimo = numeros[-1]  
i = len(numeros) - 1
while i > 0:
    numeros[i] = numeros[i-1]  
    i -= 1
numeros[0] = ultimo  
print("Lista rotada una posición a la derecha:")
i = 0
while i < len(numeros):
    print(numeros[i], end=" ")
    i += 1
print()

#ejercicio 7

temperaturas = []
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for i in range(7):
    minima = float(input(f"Ingrese la temperatura mínima del {dias_semana[i]}: "))
    maxima = float(input(f"Ingrese la temperatura máxima del {dias_semana[i]}: "))
    temperaturas.append([minima, maxima])
print("\nTemperaturas registradas:")
for i in range(7):
    print(f"{dias_semana[i]}: Mín {temperaturas[i][0]}, Máx {temperaturas[i][1]}")
suma_min = 0
suma_max = 0
i = 0
while i < 7:
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]
    i += 1
promedio_min = suma_min / 7
promedio_max = suma_max / 7
print(f"\nPromedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")
mayor_amplitud = temperaturas[0][1] - temperaturas[0][0]
indice_mayor = 0
i = 1
while i < 7:
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        indice_mayor = i
    i += 1
print(f"\nEl día con mayor amplitud térmica fue {dias_semana[indice_mayor]} con {mayor_amplitud} grados.")

#ejercicio 8

notas = []
materias = ["Matemática", "Lengua", "Historia"]
for i in range(5):
    fila = []
    print(f"\nIngresando notas del estudiante {i+1}:")
    for j in range(3):
        nota = float(input(f"Ingrese la nota de {materias[j]}: "))
        fila.append(nota)
    notas.append(fila)
print("\nPromedio por estudiante:")
for i in range(5):
    suma = 0
    j = 0
    while j < 3:
        suma += notas[i][j]
        j += 1
    promedio = suma / 3
    print(f"Estudiante {i+1}: {promedio:.2f}")
print("\nPromedio por materia:")
for j in range(3):
    suma = 0
    i = 0
    while i < 5:
        suma += notas[i][j]
        i += 1
    promedio = suma / 5
    print(f"{materias[j]}: {promedio:.2f}")

#ejercicio 9

tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero():
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()  
jugador_actual = "X"
turnos = 0
while turnos < 9:
    print(f"\nTurno del jugador {jugador_actual}")
    mostrar_tablero()
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        turnos += 1
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("La casilla ya está ocupada. Intente otra vez.")
    print("\nTablero actualizado:")
    mostrar_tablero()

#ejercicio 10

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = []
for i in range(4):
    fila = []
    print(f"\nIngresando ventas de {productos[i]}:")
    for j in range(7):
        cantidad = int(input(f"Ventas del {dias[j]}: "))
        fila.append(cantidad)
    ventas.append(fila)
print("\nTotal vendido por cada producto:")
for i in range(4):
    total_producto = 0
    j = 0
    while j < 7:
        total_producto += ventas[i][j]
        j += 1
    print(f"{productos[i]}: {total_producto}")
ventas_por_dia = []
for j in range(7):
    total_dia = 0
    i = 0
    while i < 4:
        total_dia += ventas[i][j]
        i += 1
    ventas_por_dia.append(total_dia)
max_ventas = ventas_por_dia[0]
indice_max = 0
i = 1
while i < 7:
    if ventas_por_dia[i] > max_ventas:
        max_ventas = ventas_por_dia[i]
        indice_max = i
    i += 1
print(f"\nDía con mayores ventas totales: {dias[indice_max]} ({max_ventas} unidades)")
total_por_producto = []
for i in range(4):
    total = 0
    j = 0
    while j < 7:
        total += ventas[i][j]
        j += 1
    total_por_producto.append(total)
max_producto = total_por_producto[0]
indice_producto = 0
i = 1
while i < 4:
    if total_por_producto[i] > max_producto:
        max_producto = total_por_producto[i]
        indice_producto = i
    i += 1
print(f"Producto más vendido en la semana: {productos[indice_producto]} ({max_producto} unidades)")
