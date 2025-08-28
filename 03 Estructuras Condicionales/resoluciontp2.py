#ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print(f"Es mayor de edad")

#ejercicio 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print(f"Aprobado")
else:
    print(f"Desaprobado")

#ejercicio 3

num = int(input("Ingrese un número par: "))

if num % 2 == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par")

#ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print(f"Niño/a")
elif edad >= 12 and edad < 18:
    print(f"Adolescente")
elif edad >= 18 and edad < 30:
    print(f"Adulto/a joven")
else:
    print(f"Adolto/a")

#ejercicio 5

contrasena = input("Ingrese su contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6

import random
from statistics import mode, median, mean 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mi_moda = mode(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)
mi_media = mean(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Moda: {mi_moda}")
print(f"Mediana: {mi_mediana}")
print(f"Media: {mi_media:.2f}")

if mi_media > mi_mediana > mi_moda:
    print("La distribución presenta sesgo positivo o a la derecha).")
elif mi_media < mi_mediana < mi_moda:
    print("La distribución presenta sesgo negativo o a la izquierda).")
else:
    print("No hay sesgo en este caso.")

#ejercicio 7

frase = input("Ingrese una frase: ")

if frase[-1].lower() in "aeipu":
    frase += "!"

print(f"{frase}")

#ejercicio 8 

nombre = input("Ingrese su nombre: ")

print("Seleccione una opción")
print("1 para su nombre en mayúsculas")
print("2 para su nombre en minúsculas")
print("3 para que la primer letra sea en mayúscula")

opcion = input("Ingrese 1, 2 0 3: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Incorrecto, ingrese 1, 2 o 3!")

#ejercicio 9

terremoto = float(input("Ingrese la magnitud de un terremoto: "))

if terremoto < 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy fuerte")
elif terremoto >= 7:
    print("Extremo")
else:
    print("Ingrese un valor permitido")

#ejercicio 10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el mes en número (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    sur = "Invierno"
else:
    sur = "Primavera"  # (desde 21/09 hasta 20/12)

if sur == "Verano":
    norte = "Invierno"
elif sur == "Otoño":
    norte = "Primavera"
elif sur == "Invierno":
    norte = "Verano"
else:
    norte = "Otoño"

if hemisferio == "S":
    print(f"En el hemisferio sur, la estación es: {sur}")
elif hemisferio == "N":
    print(f"En el hemisferio norte, la estación es: {norte}")
else:
    print("Hemisferio inválido. Debe ingresar N o S.")