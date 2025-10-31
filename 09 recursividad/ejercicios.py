#ejercicio 1

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

num = int(input("Ingresá un número: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#ejercicio 2

def fibonacci(n):
    if n <= 1:  
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

pos = int(input("Ingresá hasta qué posición querés ver la serie de Fibonacci: "))
for i in range(pos):
    print(fibonacci(i), end=" ")

#ejercicio 3

def potencia(base, exponente):
    if exponente == 0:  
        return 1
    else:
        return base * potencia(base, exponente - 1)  

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

#ejercicio 4

def decimal_a_binario(n):
    if n == 0:  
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  

numero = int(input("Ingresá un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")

#ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:  
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])  

texto = input("Ingresá una palabra sin espacios ni tildes: ").lower()
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

#ejercicio 6

def suma_digitos(n):
    if n < 10:  
        return n
    else:
        return n % 10 + suma_digitos(n // 10)  

num = int(input("Ingresá un número entero positivo: "))
print(f"La suma de los dígitos de {num} es {suma_digitos(num)}")

#ejercicio 7

def contar_bloques(n):
    if n == 1:  
        return 1
    else:
        return n + contar_bloques(n - 1)  

niveles = int(input("Ingresá el número de bloques en el nivel más bajo: "))
print(f"Se necesitan {contar_bloques(niveles)} bloques en total para la pirámide.")

#ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:  
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Ingresá un número entero positivo: "))
d = int(input("Ingresá el dígito que querés contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}.")
