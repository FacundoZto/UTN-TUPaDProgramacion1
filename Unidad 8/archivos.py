"""
Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
"""
print("Ejercicio 1: \n")

with open("productos.txt", "w") as archivo:
  archivo.write("Nombre,Precio,Cantidad\n")
  archivo.write("Lapicera,1.20,100\n")
  archivo.write("Hojas,0.80,150\n")
  archivo.write("Carpetas,1.50,200\n")
  print("Archivo productos.txt creado exitosamente.")

"""
Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""
print("\n Ejercicio 2: \n")

with open("productos.txt", "r") as archivo:
  #Leer encabezados
  columna_nombre, columna_precio, columna_cantidad = archivo.readline().strip().split(",")
  print(f"{columna_nombre} | {columna_precio} | {columna_cantidad}")

  #Leer filas de productos
  filas = archivo.readlines()
  for fila in filas:
    nombre, precio, cantidad = fila.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


"""
Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""
print("\n Ejercicio 3: \n")

with open("productos.txt", "r") as archivo:
  #Leer encabezados
  columna_nombre, columna_precio, columna_cantidad = archivo.readline().strip().split(",")
  print(f"{columna_nombre} | {columna_precio} | {columna_cantidad}")

  #Leer filas de productos
  filas = archivo.readlines()
  for fila in filas:
    nombre, precio, cantidad = fila.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

  # Agregar nuevo producto
  agregar = input("Desea agregar un nuevo producto? (s/n): ").strip().lower()

  if agregar == "s":
    nuevo_nombre = input("Ingrese el nombre del producto: ").strip()
    nuevo_precio = input("Ingrese el precio del producto: ").strip()
    nueva_cantidad = input("Ingrese la cantidad del producto: ").strip()
    
    with open("productos.txt", "a") as archivo_nuevo:
      archivo_nuevo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

    print("Producto agregado exitosamente.")

  elif agregar == "n":
    print("No se agregó ningún producto.")

  else:
    print("Opción no válida. No se agregó ningún producto.")


"""
Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""
print("\n Ejercicio 4: \n")

productos = []

with open("productos.txt", "r") as archivo:
  # Columnas
  columna_nombre, columna_precio, columna_cantidad = archivo.readline().strip().split(",")

  # Filas
  filas = archivo.readlines()

  for fila in filas:
    nombre, precio, cantidad = fila.strip().split(",")
    producto = {
      "nombre": nombre,
      "precio": float(precio),
      "cantidad": int(cantidad)
    }
    productos.append(producto)

print("Lista de diccionarios: ", productos)


"""
Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
"""
print("\n Ejercicio 5: \n")

producto_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()

if producto_buscado:
  with open("productos.txt", "r") as archivo:

    # Leer filas de productos
    filas = archivo.readlines()
    for fila in filas:
      encontrado = False
      nombre, precio, cantidad = fila.strip().split(",")

      if nombre.strip().lower() == producto_buscado:
        print(f"Producto encontrado: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        encontrado = True
        break

    if not encontrado:
      print("Producto no encontrado.")


"""
Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""
print("\n Ejercicio 6: \n")

with open("productos.txt", "w") as archivo_actualizado:
  # Escribir encabezados
  archivo_actualizado.write("Nombre,Precio,Cantidad\n")

  # Escribir productos desde la lista de diccionarios
  for producto in productos:
    archivo_actualizado.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo productos.txt actualizado exitosamente.")