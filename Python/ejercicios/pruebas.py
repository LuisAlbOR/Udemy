import numpy as np
import collections as collect
import math

A=['1','2','3']

for a in A:

    print(2*a)

lista = [20,50,"Curso","Python",3.14]

print(lista)

datoUno = str(input("Ingrese un dato \n"))
datoDos = str(input("Ingrese otro dato \n"))

lista[:2] = [datoUno,datoDos]

print("Lista actializada : {}".format(lista))

#Prubeas de Pila
apilar = [1,2,3,4,5]
print(apilar)

apilar.append('Hola')
apilar.append(20)
apilar.append(100)

print(apilar)

apilar.pop() #Método para quita el último item de la pila

print(apilar)

#Pruebas de Colas
colas = collect.deque() #se crea la cola

print(colas)
print(type(colas))
colas = collect.deque(['Alvaro', 'OH', 'GG', 'WP'])

print(colas)

colas.pop()
print(colas)

colas.popleft()
print(colas)

#Practicando entradas del teclado
#se pueden guardar desde la terminal distintos datos en una lista

ListaDos = [] #Se crea una lista vacía para almacenar los datos

for i in range(5): #El rango puede ser N, dependiendo de la cantidad de datos a almacenar
    ListaDos.append(input("\nIngrese datos: "))

print(ListaDos) #Se imprime la lista para verificar los valores

#Ejercicio
'''
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen,
el usuario debe ingresar los valores de “a”, “b” y “c”,
y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c= float(input("Ingrese el valor de c: "))

#Se definen los dos resultados inicializados en 0
x1 = 0
x2 = 0

#Se definen las dos condiciones de la fórmula general
if ((b**2) - (4*a*c)) < 0:
    print("No se puede realizar")
else:
    x1 = ( -b + math.sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = ( -b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    print("La solución es: \n x1 = ",x1,"\n x2 = ",x2)

#formas de salida por pantalla
variable = 'Guicho'
otraVariable = 'Unach'

forma = "El alumno '{}' forma parte de '{}'".format(variable,otraVariable)
print(forma)

forma = "El alumno '{1}' forma parte de '{0}'".format(variable,otraVariable)
print(forma)

'''
Ejercicio
Escribir un programa que solicite al usuario un vocal en minuscula,
y luego una letra en mayúsculas.
El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final,
deben ser concatenadas ambas
'''

vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

print("Tu vocal es: {}, tu letra es: {}, y la concatenación es: {}".format(vocal.upper(),letra.lower(),vocal.upper()+letra.lower()))

