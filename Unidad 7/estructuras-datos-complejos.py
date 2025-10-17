#Datos complejos

print("Ejercicio 1 \n")
"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)


print("\n Ejercicio 2 \n")
"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


print("\n Ejercicio 3 \n")
"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
frutas = list(precios_frutas.keys())
print(frutas)


print("\n Ejercicio 4 \n")
"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
agenda_telefonica = {}

for i in range(6):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero

print(agenda_telefonica)

nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")

if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta}")


print("\n Ejercicio 5 \n")
"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
print("Frase ingresada:", frase)
print("Palabras:", palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Contador de palabras:", contador_palabras)


print("\n Ejercicio 6 \n")
"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print('Diccionario alumnos: ', alumnos)

for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")


print("\n Ejercicio 7 \n")
"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
parcial1 = {"Ana", "Luis", "María", "Julián"}
parcial2 = {"María", "Julián", "Pedro"}

print('Aprobados parcial 1: ', parcial1)
print('Aprobados parcial 2: ', parcial2)

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)


print("\n Ejercicio 8 \n")
"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe
"""
stock_productos = {}

while True:
    accion = input("¿Qué acción desea realizar? (consultar/agregar/salir): ").strip().lower()
    
    if accion == "consultar":
        producto = input("Ingrese el nombre del producto a consultar: ").strip().lower()
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el stock.")
    
    elif accion == "agregar":
        producto = input("Ingrese el nombre del producto a agregar o actualizar: ").strip().lower()
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f"Se han agregado {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}")
        else:
            stock_productos[producto] = cantidad
            print(f"Se ha agregado un nuevo producto {producto} con un stock de {cantidad}.")
    
    elif accion == "salir":
        print("Saliendo del programa.")
        break
    
    else:
        print("Acción no reconocida. Por favor, ingrese 'consultar', 'agregar' o 'salir'.")
    
    print("Stock actual:", stock_productos)


print("\n Ejercicio 9 \n")
"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
"""
agenda = {}

while True:
    accion = input("¿Qué acción desea realizar? (agregar/consultar/salir): ").strip().lower()
    
    if accion == "agregar":
        dia = input("Ingrese el día del evento (formato DD/MM): ").strip()
        hora = input("Ingrese la hora del evento (formato HH:MM): ").strip()
        evento = input("Ingrese el nombre del evento: ").strip()
        agenda[(dia, hora)] = evento
        print(f"Evento '{evento}' agregado para el {dia} a las {hora}.")
    
    elif accion == "consultar":
        dia = input("Ingrese el día del evento a consultar (formato DD/MM): ").strip()
        hora = input("Ingrese la hora del evento a consultar (formato HH:MM): ").strip()
        clave = (dia, hora)
        if clave in agenda:
            print(f"El evento programado para el {dia} a las {hora} es: {agenda[clave]}")
        else:
            print(f"No hay eventos programados para el {dia} a las {hora}.")
    
    elif accion == "salir":
        print("Saliendo de la agenda.")
        break
    
    else:
        print("Acción no reconocida. Por favor, ingrese 'agregar', 'consultar' o 'salir'.")
    
    print("Agenda actual:", agenda)


print("\n Ejercicio 10 \n")
"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima"
}

capitales_paises = {}
print(paises_capitales.items())
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original (países y capitales):", paises_capitales)
print("Diccionario invertido (capitales y países):", capitales_paises)