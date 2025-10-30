#ejercicio1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#ejercicio2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))

#ejercicio3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#ejercicio4

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

#ejercicio5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa la cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas.")

#ejercicio6

def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingresa un número: "))
tabla_multiplicar(num)

#ejercicio7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#ejercicio8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#ejercicio9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

#ejercicio10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")