# Práctico 1 - Estructuras secuenciales

# Ejercicio 1
print("Ejercicio 1")
print("Hola Mundo!")

# Ejercicio 2
print("Ejercicio 2")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
print("Ejercicio 3")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
print("Ejercicio 4")
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5
print("Ejercicio 5")
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas.")

# Ejercicio 6
print("Ejercicio 6")
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
print("Ejercicio 7")
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
else :
    print("Ambos números deben ser distintos de 0.")

# Ejercicio 8
print("Ejercicio 8")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

# Ejercicio 9
print("Ejercicio 9")
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")

# Ejercicio 10
print("Ejercicio 10")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")
