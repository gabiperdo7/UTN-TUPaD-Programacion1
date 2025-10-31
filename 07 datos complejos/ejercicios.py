#ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#ejercicio 2

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#ejercicio 3

precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#ejercicio 4

agenda_telefonica = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input("Ingresá el número telefónico: ")
    agenda_telefonica[nombre] = telefono

consulta = input("Ingresá el nombre que querés consultar: ")
if consulta in agenda_telefonica:
    print(f"El número de {consulta} es {agenda_telefonica[consulta]}")
else:
    print("El contacto no existe en la agenda.")

#ejercicio 5

frase = input("Ingresá una frase: ")

palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Cantidad de apariciones:", conteo)

#ejercicio 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

#ejercicio 7

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#ejercicio 8 

stock = {
    "Clavos": 100,
    "Martillo": 25,
    "Madera": 50
}

producto = input("Ingresá el nombre del producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades agregás?: "))
        stock[producto] += cantidad
        print("Stock actualizado:", stock)
else:
    print("El producto no existe. Se agregará al inventario.")
    cantidad = int(input("¿Cuántas unidades tiene?: "))
    stock[producto] = cantidad
    print("Producto agregado:", stock)

#ejercicio 9

agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de programación",
    ("Viernes", "18:00"): "Gimnasio"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (formato 00:00): ")

if (dia, hora) in agenda:
    print(f"A esa hora tenés: {agenda[(dia, hora)]}")
else:
    print("No hay actividad registrada en ese horario.")

#ejercicio 10

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales = {capital: pais for pais, capital in paises.items()}

print(capitales)
