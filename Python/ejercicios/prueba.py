print("Hello world on python")

#comentario de una sola linea en python
#no es necesario el ';'

'''
comentarios de varias
lineas de código
'''

#se puede cambiar el  tipo de dato de una variable indiscriminadamente
dato = 10
print(type(dato))  #comprueba el tipo de dato
dato = "Ojeto"
print(type(dato))
dato = True
print(type(dato)) #así con N tipo de dato

#sumas aritmeticas
n1 = 1
n2 = 2
r = n1 + n2
print(r)

#resta aritmetica
n1 = 3
n2 = 2
r = n1 - n2
print(r)

#multiplicación aritmetica
n1 = 1
n2 = 2
r = n1 * n2
print(r)

#división aritmetica
n1 = 1
n2 = 2
r = n1 / n2
print(r)

#negación aritmetica
n1 = 1
n2 = 2
r = n1 - n2
print(r)

#potencia aritmetica
n1 = 2
n2 = 4
r = n1 ** n2
print(r)

#división entera, solo devuelve el entero de la división
n1 = 3
n2 = 2
r = n1 // n2
print(r)

#módulo, solo devuelve el residuo de la división
n1 = 3
n2 = 6
r = n1 % n2
print(r)

#operación matemática simple
r = (5+9/3)**2
print(r)

'''''
los operadores de comparación y sus sintaxis es el mismo que todos los lenguajes:

    ==
    >
    <
    >=
    <=
    !=

    ejemplos:
a==b
a>b
a<b
a>=b
a<=b
a!=b

'''''

#operadores lógicos: and -> or -> not
a = 10
b = 20
c = 30
r = ((a<b) and (b<c))
print(r)
r = ((a>b) or (b<c))
print(r)
r= not((a<b) and (b<c))
print(r)

#operadores de asignación
i = 0
print(i)
i +=10
print(i)
i -=5
print(i)
i *=3
print(i)
i /= 5
print(i)
i **=3
print(i)
i %=3
print(i)

#salida de datos
app = "GG"
modulo = "WP"
print(f"se añade al aplicativo {app} el módulo {modulo}") # sirve la 'F' antes de las comillas para decirle al compilador que tendra una salida de datos de una variable

#entrada de datos
cadena = input("GG? ") #Al parecer despues del '?' es posible saltar la entrada de datos de la terminal
print(f"{cadena} WP")

'''''
Cabe recalcar que si se ingresa una cadena la varible cadena sera de tipo 'str' por lo que no se podrán
hacer operaciones aritmeticas con dicha variable, ahora es momento de convertir la entrada de datos a
uno de tipo númerico
'''''

cadena = int(input("Ingrese un numero: "))
print(f"Sumando +1 es: {cadena+1}")

'''''
Asi tambien se puede convertir la cadena que se recibe en cualquier tipo de datos númerico:
float
double
int

Con esto termina la introduccion basica a python y su sintaxis en las operaciones basicas, aqui algunas
notas:
1.- hay que cuidar las tabulaciones porque el compilador de python si lee las tabulaciones y las interpreta,
si miras detalladamente, todo el codigo no tiene tabulaciones o espacios para tener una mejor interpretacion,
esto para evitar errores.
Para python no es lo mismo:
cadena = int(input("Ingrese un numero: "))
print(f"Sumando +1 es: {cadena+1}")

que:
cadena = int(input("Ingrese un numero: "))
    print(f"Sumando +1 es: {cadena+1}")

lo interpreta de manera diferente, por eso hay que cuidar las tabulaciones.

2.- en python no es necesario finalizar una linea de codigo con ';' porque el compilador lo hace por nosotros,
o mejor dicho c-sharp, asi que no hay que preocuparse por ese error.

3.- hay que cuidar el orden de '()' para evitar conflictos en las formulas matematicas y sus operaciones,
cabe recalcar que para hacer las operaciones matematicas hay que el uso de '*' ya que python no interpreta
el uso de '()()' para hacer multiplicaciones
'''''
