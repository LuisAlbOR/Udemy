nombre1 = input("Ingrese un nombre: ")
nombre2 = input("Ingrese otro nombre: ")

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia")

'''
Explicacion:
Se sabe que lo que obtendras de un input es una cadenas, asi que para
obtener cualqier valor tendras que manejarlo como cualquier cadena con
sus indices, y para obtener el primer caracter de X cadena solo tienes
que especificar el indice 0 que es el primero.
Ahora para obtener el ultimo caracter de cualquier cadena, solo tienes
que poner el indice -1 entre los parentesis
'''