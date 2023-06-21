
#Ejercicio verificando si riman las palabras por defecto
cadena = 'Lolsito'
palabra = "lolsito"

print(cadena[:2])
print(cadena[-3:])
print(cadena[::2])
print(cadena[::-1])
print(cadena + cadena[::-1])

if cadena[-3:] == palabra[-3:]:
    print("riman los loleros \n")

#ejercicio verificando si es vocal

letra = input("Ingrese un caracter \n")

if letra == 'a':
    print("Es una vocal")
elif letra == 'e':
    print("Es una vocal")
elif letra == 'i':
    print("Es una vocal")
elif letra == 'o':
    print("Es una vocal")
elif letra == 'u':
    print("Es una vocal")
else:
    print("Es otra letra")
    
print(letra)

#Comparando las tres y dos últimas letras de dos palabras para ver si combinan, también si combinan
cadenaUno = input("\n Ingresa una palabra che\n")
cadenaDos = input("\n Ingresa otra palabra che\n")

if cadenaUno[-3:] == cadenaDos[-3:]:
    print("\n Riman de maravila")
elif cadenaUno[-2:] == cadenaDos[-2:]:
    print("\n Riman poco pero de sabroso")
else:
    print("\n No tienes imaginación")
    
numero = int(input("\n Ingrese un número para multiplicar \n"))

#tabla de multiplicar de N número limitado a las 10 primeras multiplicaciones
iteracion = 0
while iteracion <= 10:
    print("\n",iteracion," * ",numero," = ",(iteracion*numero))
    iteracion +=1
'''
   # otra forma de hacer el ejerciio de multiplicación:
numero = int(input("\nIngrese un número: "))
i = 0

while i <= 10:
    print("{} X {} = {}".format(numero,i,(numero*i)))
    i += 1
'''