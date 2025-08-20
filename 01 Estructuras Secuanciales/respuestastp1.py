#ejercicio 1

print("Hola Mundo!")

#ejercicio 2

nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}")

#ejercicio 3

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
age = int(input("Ingrese se edad "))
nacionalidad = input("Ingrese su nacionalidad ")
print(f"Soy {nombre} {apellido}, tengo {age} años y soy de {nacionalidad}.")

#ejercicio 4

radio = float(input("Ingrese el radio del círculo: "))
pi_valor = 3.141592653589793
perimetro = 2 * pi_valor * radio
area = pi_valor * (radio * radio)
print(f"El área del círculo es: {area}, y el perímetro es: {perimetro}.")

#ejercicio 5

segundos = int(input("Ingrese la cantidad de segundos: "))
hora = segundos / 3600
print(f"La cantidad de segundos equivale a: {hora} hs.")

#ejercicio 6

num1 = int(input("Ingrese un número: "))
for i in range(1, 11):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")

#ejercicio 7

num1 = int(input("Ingrese el primer número, que no sea 0: "))
num2 = int(input("Ingrese el segundo número, tampoco puede ser 0: "))
suma = num1 + num2
division1 = num1 / num2
division2 = num2 / num1
multiplicacion = num1 * num2 
resta1 = num1 - num2 
resta2 = num2 - num1
print(f"El resultado de la suma es: {suma}. El resultado de las divisiones son: {division1} y {division2}. El resultado de la multiplicación es: {multiplicacion} y los resultados de las restas son: {resta1} y {resta2}.")

#ejercicio 8

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
masacorporal = peso/ (altura * altura)
print(f"Su masa corporal es: {masacorporal}.")

#ejercicio 9

gradosc = float(input("Ingrese los grados en Celsius: "))
gradosf = 9 / 5 * gradosc + 32
print(f"El equivalente en grados Fahrenheit es: {gradosf}.")

#ejercicio 10

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
resultado = (num1 + num2 + num3) / 3
print(f"El promedio de estos 3 números es: {resultado}.")