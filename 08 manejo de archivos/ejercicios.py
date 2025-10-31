#ejercicio 1

with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,450.0,15\n")
    archivo.write("Regla,80.0,25\n")

print("Archivo productos.txt creado correctamente.")

#ejercicio 2

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#ejercicio 3

with open("productos.txt", "r", encoding="utf-8") as archivo:
    print("Productos actuales:")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

with open("productos.txt", "a", encoding="utf-8") as archivo:
    nombre = input("Nombre del nuevo producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado correctamente.")

#ejercicio 4

productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

print("Lista de productos cargada:")
for p in productos:
    print(p)

#ejercicio 5

productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

buscado = input("Ingresá el nombre del producto que querés buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe en la lista.")

#ejercicio 6

productos = [
    {"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
    {"nombre": "Cuaderno", "precio": 450.0, "cantidad": 15},
    {"nombre": "Regla", "precio": 80.0, "cantidad": 25}
]

productos.append({"nombre": "Goma", "precio": 50.0, "cantidad": 40})

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo productos.txt actualizado con los nuevos datos.")
