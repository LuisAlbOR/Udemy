import math as mt
import os

def limpiarPantalla():
    #Comando para limpiar pantalla en la terminal de dependiendo del OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#En este archivo se encuentran todos los ejercicios que tengan que ver cn funciones
#Así se define una funcion en Python 3
'''
def holaMundo():
    print("Hello World!")
    
holaMundo() #Importante recordar que al llamar un funcion tenemos que especificar
            #que es una agregandole los parentesis al final
            
#Funcion que imprime las diez primeras multiplicaciones de un numero por defecto
def tablaDeMultipicar():
    for i in range(10):
        print("\n {} X {} = {}".format(i+1,7,((i+1)*7)))

tablaDeMultipicar()

'''

'''
Ejercicio
Crear un programa que tenga una lista,
luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

ListaDatos = []
datosNumericos = 0

def pedirDatos ():
    i = 0
    while i < 5:
        datosNumericos = int(input("\n Ingrese numeros enteros \n"))
        ListaDatos.append(datosNumericos)
        i+=1
        
    verificarNumeroParEImpar(ListaDatos)

def verificarNumeroParEImpar(ListaDatos: list):
    ListaDatos.sort()#mtodo que ordena de menor a mayor
    ListaNumerosPares =[]
    ListaNumerosImpares = []
    
    for i in ListaDatos:
        if i % 2 == 0:
            ListaNumerosPares.append(i)
        else:
            ListaNumerosImpares.append(i)
    
    imprimirEnPantalla("Lista de números pares: {}".format(ListaNumerosPares))
    imprimirEnPantalla("Lista de números impares:  {}".format(ListaNumerosImpares))
    

def imprimirEnPantalla(Lista: list):
    print(Lista)
    
#Se manda a llamar al metodo
pedirDatos()
'''

'''
Ejercicio
Crear una funcion que pida dos numeros.
Si el primero es mayor al segundo, el programa debe retornar el valor 1;
si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0


def pidiendoNumeros() -> int:
    n1 = int(input("\n Ingrese un numero entero: "))
    n2 = int(input("\n Ingrese otro numero entero: "))
    return compararNumeros(numeroUno=n1,numeroDos=n2)
    
    
def compararNumeros(numeroUno: int, numeroDos: int) -> int:
    if numeroUno > numeroDos:
        return 1
    elif numeroUno < numeroDos:
        return -1
    else:
        return 0

print(pidiendoNumeros())
'''

'''
#Probando que las variables que son declaradas fuera de una funcion pueden ser modificadas
#dentro de una función pero seguiran con el mismo valor fuera de ella
def funcionUno (valor):
     valor*=3

variableUno = 10
print(variableUno)
print(funcionUno(variableUno))
#No puede modificarse la varibale si no tiene un return dentro de ella para modificarse
#fuera de la funcion
def funcionDos(valor: int) -> int:
    return valor*3

variableUno = 10
print(variableUno)
print(funcionDos(variableUno))

#Pero las listas si se pueden modicar sin el valor de return
def funcionTres(lista: list) ->list:
    for i,j in enumerate(lista):
        lista[i] *= 3
        
Lista = [10,20,30]
print(Lista)
print(funcionTres(Lista))

'''

'''
#Probando funcionde donde sus argumentos son un diccionario y una lista
#Ademas de hacer fuciones que funciones por posiciones y tipo
def funcionCuatro(*tupla): #un * indica que recibirar N cantidad de argumentos
    for i in tupla:
        print(i)
        
print("\n ",funcionCuatro('Oh','GG',10,(2,'jdjd',),{23,'32'},['hola']))
#Esto fue por posición
#Ahora por nombre

def funcionCinco(**diccionario):
    for i in diccionario: #con este for imprime solo las claves de un diccionario
        print(i," : ", diccionario[i])#Se imprime la clave y el contenido
    
print("\n",funcionCinco(oh='GG',report='jg',ezz='all',kda=[10,3,13]))

def funcionSeis(*tupla,**diccionario):
    bandera = 0
    for i in tupla:
        bandera+=i
    print(bandera)
    #Pytho detecta cuando deja de recibir por posicion y empieza a recibir por nombre
    for i in diccionario:
        print(i," : ", diccionario[i])

print("\n ",funcionSeis(1,2,3,4,6,7,100,oh='GG',report='jg',ezz='all',kda=[10,3,13]))

'''

'''
Ejercicio
 Crear un programa que tenga dos funciones,
 una que contenga el area de un cuadrado con argumentos de base y altura;
 y la  otra el area de un circulo con argumento de radio

def areaCuadrado(base: float, altura: float) -> float:
    return base * altura

def areaCirculo(radio: float) -> float:
    return mt.pi * (radio**2)
    
def pedirDatosCuadrado():
    base = float(input("\n Ingrese la base del cuadrado: "))
    altura = float(input("\n Ingrese la altura del cuadrado: "))
    
    if(base < 0 or altura < 0):
        limpiarPantalla()
        print("\n No se aceptan valores menores a 0 \n")      
    else:
        limpiarPantalla()
        print("El area del cuadrado es: {}".format(areaCuadrado(base=base, altura=altura)))

def pedirDatosCirculo():
    radio = float(input("\n Ingrese el radio del circulo: "))
    
    if(radio < 0):
        limpiarPantalla()
        print("\n No se aceptan valores menores a 0 \n")
    else:
        limpiarPantalla()
        print("\n El area del circulo es: {}".format(areaCirculo(radio=radio)))

opcion = 0

while(opcion != 3):
    print("\nDesea saber el area de un cuadrado? Presione 1 \nDesea saber el area de un circulo? Presione 2 \nDesea sali? Presione 3")
    opcion = int(input())
    
    if(opcion == 1):
        limpiarPantalla()
        pedirDatosCuadrado()
    elif(opcion == 2):
        limpiarPantalla()
        pedirDatosCirculo()
    else:
        limpiarPantalla()
        print("Hasta la proxima...")
'''

#Ejemplo de funcion recursiva, funion de cuenta regresiva
'''
def cuentaRegresiva(valor:int)->int:
    valor -= 1
    
    if valor >= 0:
        print(valor)
        cuentaRegresiva(valor)
    else:
        print("\nHa terminado la cuent regresiva")
        
cuentaRegresiva(10)
'''
