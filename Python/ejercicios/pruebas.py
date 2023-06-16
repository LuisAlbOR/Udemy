import numpy as np
A=['1','2','3']

for a in A:

    print(2*a)

lista = [20,50,"Curso","Python",3.14]

print(lista)

datoUno = str(input("Ingrese un dato \n"))
datoDos = str(input("Ingrese otro dato \n"))

lista[:2] = [datoUno,datoDos]

print("Lista actializada : {}".format(lista))