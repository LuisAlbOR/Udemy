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
A=['1','2','3']

for a in A:
    print(2*a)

#ejercicio con tupla
#Escribir una tupla con los meses del año, luego, pide al usuario un numero,
#el que haya ingresado, es el mes que debe mostrar en la tupla

mesesDelAño = meses=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

numeroDelMes = int(input(" \n Ingrese el numero del mes \n"))

print(mesesDelAño[numeroDelMes - 1])

#conjuntos
conjunto = {'pa','pa','pa',1,3,4,5,6,7,7,'a','b','y','h','e'}

print(conjunto)

conjunto.add('c')

print(conjunto)

Lista = ['hola', 'hola' , 'Hola', 2,3,5,',',';',1231.1321]

print(Lista)

conuntoLista = set(Lista)

#otro ejemplo del metodo SET
cadena = "GG WP reporten al JG, TEAM DIFF, SUBANLE LA DIFICULTAD A LOS BOTS, EZZZZZZ TOP"

print(set(cadena))

'''
    Ejercicio de diccionario
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario,
y muestre la capital de ese pais, en dado caso el pais no este en el diccionario,
se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

diccionarioCapitales = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

nombrePaisNoAceptable = input("\n Ingrese el  nombre de un país: \n")

#El método capitalize() vuelve la primer letra de una palabra mayuscúla
#print(nombrePais.capitalize())
nombrePaisAceptable = nombrePaisNoAceptable.capitalize()
resultadoBusqueda = nombrePaisAceptable in diccionarioCapitales

if resultadoBusqueda == True:
    print(diccionarioCapitales[nombrePaisAceptable])
else:
    print("Su país no esta dentro del diccionario")