#En este archivo se encuentran todos los ejercicios que tengan que ver cn funciones
#Así se define una funcion en Python 3
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
Ejercicio
Crear un programa que tenga una lista,
luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''