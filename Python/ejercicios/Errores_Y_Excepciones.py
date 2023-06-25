#En este archivo se tienen ejemplos para el manejo de excepciones y errores en pytho 3

#Lo siguiente es un error de tipo, eso significa que el input es incorrecto
'''
datoEntrada = int(input("Ingresa algo: "))
'''
#El error que se muestra es que se ingreso algo que no es un entero
#El mensaje es legible para personas que entienden la programación (o eso se espera)
#pero las personas normales no entenderian, asi que para eso se hace lo siguiente
'''
try:
    codigo python que hace algo
except:
    codigo python que se ejecuta si algo scoope de TRY salio mal

#Ejemplo
try:
    datoEntrada = int(input("\n Inngrese un entero: "))
    print("{} X {} = {}".format(datoEntrada, 2,(datoEntrada*2)))
except:
    print("\n mamahuevo igresaste otra cosa que no es entero")
'''  
#Para mejorar el código se puede ingresar en un ciclo while
#PERO NO SE OLVIDE QUE TIENE QUE ROMPER EL WHILE PARA NO CRASHEAR SI PC
'''
while(True):
    try:
        datoEntrada = int(input("\n Inngrese un entero: "))
        print("{} X {} = {}".format(datoEntrada, 2,(datoEntrada*2)))
        break #PARA SALIR DEL CICLO SI SE CUMPLE
    except:
        print("\n mamahuevo igresaste otra cosa que no es entero")

'''
#Para mejorar aún más el código se puede agregar un 'Si se cumple correctamente'
'''
try:
    codigo python 3
except:
    codigo python 3 donde se maneja la exceptio
else:
    codigo python 3 si se ejecuta correctamente
#Ejemplo
while(True):
    try:
        datoEntrada = int(input("\n Ingrese un entero: "))
        print("{} X {} = {}".format(datoEntrada,2,(datoEntrada*2)))
    except:
        print("\n mamahuevo igresaste otra cosa que no es entero")
    else:
        print("Veo que tienes buena compresion lectora...") 
        break#Ahora se pone el break ya que aca se hizo todo correcto
'''
#Ahora hay otra cosa que se puede agregar, el 'finally'
#Este se ejecuta independientemente si hay una exception o no
'''
#Ejemplo
while(True):
    try:
        datoEntrada = int(input("\n Ingrese un entero: "))
        print("{} X {} = {}".format(datoEntrada,2,(datoEntrada*2)))
    except:
        print("\n mamahuevo igresaste otra cosa que no es entero")
    else:
        print("Veo que tienes buena compresion lectora...") 
        break#Ahora se pone el break ya que aca se hizo todo correcto
    finally:
        print("\n OHGG")
'''
'''
Ahora si bien podemos controlar nosotros las excepciones, hay casos
donde pueden ocurrir varias excepciones, para estos casos se usan 
multiples excepciones, pueden suceder por datos de entrada o al hacer
operaciones en una función
try:
    datoEntrada = input("\n Numerp: ")
    print(datoEntrada/10)
except Exception as exception:
    print(type(exception).__name__)#Esto se vera en el tema POO
'''
'''
Sin embargo en el ejemplo de arriba, solo marca que hay un error, no
indica de que o donde ocurre, ahora se vera el manejo de muchas excepciones
#Ejemplo
try:
    datoEntrada = float(input("Numero: "))
    print(10/datoEntrada)
except TypeError:
    print("\n Esto es una")
except ValueError:
    print("\n El tipo debe ser numero")
except ZeroDivisionError:
    print("\n No se puede dividir entre 0")
except Exception as exception:
    raise(type(exception).__name__)
'''
'''
Ahora bien nosotro podemos definir nuestras propias excepciones: un metodo
def funcionExcepcion(valor=None):
    if valor is None:
        print("Debes escribir algo, si no, no llames a la función")
        
print(funcionExcepcion())
'''
'''
Ahora puedes modificar el identificador del error , con la funccion RASIE
ejemplo
def funcionExcepcion(valor=None):
    if valor is None:
        raise ValueError("Debes escribir algo, si no, no llames a la funcion")

print(funcionExcepcion())
Se puede ver que se modifico el mensaje de error del ValueError, eso hace
que aunque un usuario normal use el programa y tire el error mas feo del
mundo, pueda ser legible por cualquier persona
'''