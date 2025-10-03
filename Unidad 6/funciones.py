print("\n Ejercicio 1 \n")
"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

print("\n Ejercicio 2 \n")
"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
nombre_usuario = input("Ingrese su nombre: ")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

print(saludar_usuario(nombre_usuario))

print("\n Ejercicio 3 \n")
"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

informacion_personal(nombre, apellido, edad, residencia)

print("\n Ejercicio 4 \n")
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
pi = 3.141592653589793
radio = float(input("Ingrese el radio del círculo: "))

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

print("\n Ejercicio 5 \n")
"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
segundos = int(input("Ingrese la cantidad de segundos: "))

def segundos_a_horas(segundos):
    return round(segundos / 3600, 2)

print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

print("\n Ejercicio 6 \n")
"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro e imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(numero)

print("\n Ejercicio 7 \n")
"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
"""
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (no se puede dividir por cero)"
    operaciones = (suma, resta, multiplicacion, division)
    return operaciones

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]} | Resta: {resultados[1]} | Multiplicación: {resultados[2]} | División: {resultados[3]}")

print("\n Ejercicio 8 \n")
"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

print(f"Su índice de masa corporal (IMC) es: {calcular_imc(peso, altura)}")

print("\n Ejercicio 9 \n")
"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

print(f"{celsius} grados Celsius son {celsius_a_fahrenheit(celsius)} grados Fahrenheit.")

print("\n Ejercicio 10 \n")
"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)

print(f"El promedio de {a}, {b} y {c} es: {calcular_promedio(a, b, c)}")