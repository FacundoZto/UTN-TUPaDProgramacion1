# Práctico 3: Estructuras condicionales

import random
from statistics import mode, median, mean


print("Ejercicio 1")

edad = int(input("Ingrese su edad: "))
if edad > 18:
  print("Es mayor de edad")


print("Ejercicio 2")

nota = float(input("Ingrese su nota: "))
if nota >= 6:
  print("Aprobado")
else:
  print("Desaprobado")


print("Ejercicio 3")

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")


print("Ejercicio 4")

edad = int(input("Ingrese su edad: "))
if edad < 12:
  print("Niño/a")
elif edad >= 12 and edad < 18:
  print("Adolescente")
elif edad >= 18 and edad < 30:
  print("Adulto/a joven")
else:
  print("Adulto/a")


print("Ejercicio 5")

contrasena = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


print("Ejercicio 6")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if (media > mediana) and (mediana > moda):
  print("Sesgo positivo") 
elif (media < mediana) and (mediana < moda):
  print("Sesgo negativo")
elif media == mediana == moda:
  print("No hay sesgo") 


print("Ejercicio 7")

palabra = input("Ingrese una frase o palabra: ")
letra_final = palabra[len(palabra) - 1].lower()
if letra_final in "aeiou":
  print(palabra + "!")
else:
  print(palabra)



print("Ejercicio 8") 

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 si quiere su nombre en mayúsculas, 2 si quiere su nombre en minúsculas o 3 si quiere su nombre con la primera letra mayúscula: "))
if opcion == 1:
  print(nombre.upper())
elif opcion == 2:
  print(nombre.lower())
elif opcion == 3:
  print(nombre.title())



print("Ejercicio 9")

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3:
  print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
  print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")
else:
  print("Extremo (puede causar graves daños a gran escala)")


print("Ejercicio 10")

hemisferio = input("Ingrese N o S según el hemisferio en el que se encuentra: ").lower()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

if hemisferio == "n":
  if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
    print("Invierno")
  elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
    print("Primavera")
  elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 23):
    print("Verano")
  elif (mes == 9 and dia >= 23) or (mes <= 12 and dia < 21):
    print("Otoño")
elif hemisferio == "s":
  if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
    print("Verano")
  elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
    print("Otoño")
  elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 23):
    print("Invierno")
  elif (mes == 9 and dia >= 23) or (mes <= 12 and dia < 21):
    print("Primavera")
else:
  print("Hemisferio no válido")