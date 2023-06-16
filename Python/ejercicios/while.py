#bucle while
import math

numero = int(input("Ingrese un entero: "))

while numero<1:
    print("Por favor ingrese un numero positivo")
    numero= int ( input("Ingrese un numero positivo: "))

print(f"La raiz cuadrada es {math.sqrt(numero):.2}")

A=['1','2','3']

for a in A:
    print(2*a)

