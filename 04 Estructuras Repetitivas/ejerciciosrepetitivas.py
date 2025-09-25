#ejercicio 1

for i in range(0, 101):
    print(i)

#ejercicio 2

numero = input("Ingrese un número entero: ")
if numero.startswith('-'):
    numero = numero[1:]
cantidad_digitos = len(numero)
print(f"El número tiene {cantidad_digitos} dígito(s).")

#ejercicio 3

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
if inicio > fin:
    inicio, fin = fin, inicio  
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los números entre {inicio} y {fin} (excluyendo los extremos) es: {suma}")

#ejercicio 4

total = 0  
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:  
        break
    total += numero  
print(f"La suma total es: {total}")

#ejercicio 5

import random  
numero_secreto = random.randint(0, 9)
intentos = 0  
while True:
    try:
        adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    intentos += 1
    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intento(s).")
        break
    else:
        print("Número incorrecto. Intenta nuevamente.")

#ejercicio 6

for i in range(100, -1, -1):  
    if i % 2 == 0:  
        print(i)

#ejercicio 7

n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("El número ingresado no es positivo.")
else:
    suma = 0
    for i in range(n + 1):  
        suma += i
    print(f"La suma de los números desde 0 hasta {n} es: {suma}")

#ejercicio 8

cantidad = 100  
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#ejercicio 9

cantidad = 100  
suma_total = 0 
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero  
media = suma_total / cantidad
print(f"\nLa media de los {cantidad} números ingresados es: {media}")

#ejercicio 10

numero = input("Ingrese un número entero: ")
es_negativo = False
if numero.startswith('-'):
    es_negativo = True
    numero = numero[1:]  
numero_invertido = numero[::-1]
if es_negativo:
    numero_invertido = '-' + numero_invertido
print(f"El número invertido es: {numero_invertido}")
