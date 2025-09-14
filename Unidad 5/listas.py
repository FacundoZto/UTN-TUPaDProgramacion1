print("Ejercicio 1 \n")
"""
1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""
notas = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
promedio = sum(notas) / len(notas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print("Notas: \n")
for i in range(len(notas)):
    print("La nota del estudiante", i + 1, "es:", notas[i])

print("El promedio de las notas es:", promedio)
print("La nota más alta es:", nota_mas_alta)
print("La nota más baja es:", nota_mas_baja)

print()


print("Ejercicio 2 \n")
"""
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""
productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto: ").lower()
    productos.append(producto)

print("Lista ordenada:", sorted(productos))
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ").lower()

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto eliminado. Lista actualizada:", sorted(productos))
else:
    print("El producto no se encuentra en la lista.")


"""
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.
"""
print("\nEjercicio 3 \n")

import random
numeros = []

for i in range(15):
    numero = random.randint(1, 100)
    numeros.append(numero)

print("Números generados:", numeros)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Cantidad de números pares:", len(pares))
print("Números impares:", impares)
print("Cantidad de números impares:", len(impares))


"""
4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""
print("\nEjercicio 4 \n")

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista original:", datos)
nueva_lista = []

for elemento in datos:
    if elemento not in nueva_lista:
        nueva_lista.append(elemento)

print("Lista sin elementos repetidos:", nueva_lista)


"""
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""
print("\nEjercicio 5 \n")

estudiantes = []
for i in range(8):
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)

print("Estudiantes presentes en clase:", estudiantes)
pregunta = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper()

if pregunta == "A":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado. Lista actualizada:", estudiantes)
elif pregunta == "E":
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Estudiante eliminado. Lista actualizada:", estudiantes)
    else:
        print("El estudiante no se encuentra en la lista.")


"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
"""
print("\nEjercicio 6 \n")

lista_numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", lista_numeros)

nueva_lista = [0] * len(lista_numeros) # Crear una lista vacía del mismo tamaño

nueva_lista[0] = lista_numeros[-1]  # El último pasa a ser el primero
print("nueva lista", nueva_lista)

for i in range(1, len(lista_numeros)):
    print("i:", i)
    print(nueva_lista)
    nueva_lista[i] = lista_numeros[i - 1]
    print(nueva_lista)
    print()

print("Lista rotada a la derecha:", nueva_lista)


"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica
"""
print("\nEjercicio 7 \n")

temperaturas = [
    [15, 25],  # Lunes
    [17, 28],  # Martes
    [14, 22],  # Miércoles
    [16, 30],  # Jueves
    [18, 27],  # Viernes
    [19, 29],  # Sábado
    [20, 31]   # Domingo
]
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(temperaturas)):
    suma_minimas += temperaturas[i][0]
    suma_maximas += temperaturas[i][1]
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[i]

promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)
print("Promedio de temperaturas mínimas:", promedio_minimas)
print("Promedio de temperaturas máximas:", promedio_maximas)
print("Día con mayor amplitud térmica:", dia_mayor_amplitud, "con una amplitud de", mayor_amplitud, "grados.")

"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""
print("\nEjercicio 8 \n")

notas = [
    [85, 90, 78],  # Estudiante 1
    [92, 88, 84],  # Estudiante 2
    [76, 95, 89],  # Estudiante 3
    [84, 91, 87],  # Estudiante 4
    [90, 82, 80]   # Estudiante 5
]

for i in range(len(notas)):
    promedio_estudiante = sum(notas[i]) / 3
    print(f"Promedio del Estudiante {i + 1}: {round(promedio_estudiante, 2)}")

print()

for j in range(len(notas[0])):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"Promedio de la Materia {j + 1}: {promedio_materia}")


"""
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.
"""
print("\nEjercicio 9 \n")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
  ]

"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""
print("\nEjercicio 10 \n")

ventas = [
    [150, 200, 250, 300, 350, 400, 450],  # Producto 1
    [100, 150, 200, 250, 300, 350, 400],  # Producto 2
    [200, 250, 300, 350, 400, 450, 500],  # Producto 3
    [250, 300, 350, 400, 450, 500, 550]   # Producto 4
]

totales_por_producto = []
for i in range(len(ventas)):
    suma_por_producto = 0

    for j in range(len(ventas[i])):
        suma_por_producto += ventas[i][j]

    totales_por_producto.append(suma_por_producto)
    print(f"Total vendido por el Producto {i + 1}: {suma_por_producto}")

print("Totales por producto", totales_por_producto)
producto_mas_vendido = max(totales_por_producto)
indice_producto_mas_vendido = totales_por_producto.index(producto_mas_vendido) + 1  # +1 para que sea Producto 1, 2, ...
print(f"El producto más vendido en la semana fue el Producto {indice_producto_mas_vendido} con {producto_mas_vendido} ventas.")

totales_por_dia = []
for dia in range(len(ventas[0])):
    suma_dia = 0

    for producto in range(len(ventas)):
        suma_dia += ventas[producto][dia]
        """
        1er ciclo	suma_dia += ventas[0][0] 150
        2do ciclo	suma_dia += ventas[1][0] 100
        3er ciclo	suma_dia += ventas[2][0] 200
        4to ciclo	suma_dia += ventas[3][0] 250
        """

    totales_por_dia.append(suma_dia)

print("Totales por día", totales_por_dia)
mayor_ventas = max(totales_por_dia)
dia_mayor_ventas = totales_por_dia.index(mayor_ventas) + 1 
print(f"Las mayores ventas totales fueron el día {dia_mayor_ventas} de la semana, con {mayor_ventas} ventas.")