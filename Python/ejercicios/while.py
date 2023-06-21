#bucle while
import math

numero = int(input("Ingrese un entero: "))

while numero<1:
    print("Por favor ingrese un numero positivo")
    numero= int ( input("Ingrese un numero positivo: "))

print(f"La raiz cuadrada es {math.sqrt(numero):.2}")

#Operación aritmetica

numeroUno = 3
numeroDos = 2
numeroTres = 5
potencia = 2

print(((numeroUno + numeroDos)/(numeroDos*numeroTres))**potencia)
