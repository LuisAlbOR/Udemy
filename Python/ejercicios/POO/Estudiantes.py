#Se crea la clase estudiantes en python para probar POO
class Estudiantes:
    #Con esto se crea una clase vacía
    pass

Estudiantes = Estudiantes() #Así se crea un objeto en python
#Se verifica con la función type para ver que es lo que acabamos de hacer
print(type(Estudiantes))
#Ahora para ver la diferencia con un método
def Estudiante():
    pass
#Verificamos el tipo
print(type(Estudiante))

#Se pueden definir atibutos de la siguiente forma
class Auto:
    pass #Se define la clase Auto vacía

auto = Auto() #Se crea el objeto de la clase Auto
#Ahora se definiran atributos de la clase
auto.color = "Rojo" #El color del auto
auto.marca = "Masseratti" #La marca del auto
#Ahora se verificara si se guarda o no
print("mi auto de marca {} es de color {}".format(auto.marca,auto.color))
#A pesar que al poner el '.' no muestra el atributo, no ha error al compiar y ejecutar
#Ahora se vera un ejemplo para diferenciar una clase  de una función
'''
class Casa:
    Rojo = False
    
    def __init__(self):
        print("Se creo una casa")

    La explicación de el método(o función) '_ini_' es una funión interna de la clase,
    se comparte con todos los objetos de la clase y por eso lleva dos guión bajo, algo
    similiar es el método 'Constructor' en Java, se crea automaticamente el objeto al
    utilizar el '_init_', el 'Self' hace referencia al propio objeto y todos los métodos
    lo tienen y sirve para diferencias entre el ambito de clase y de un método, es un
    requisito implícito(obligatorio a la definición).
    def Fabricar(self):
        Rojo = True
casa = Casa() #Al crear el objeto se muestra el print del método '_init_'
#print(casa.Fabricar) #Hay un error si quieres acceder al método y modificar los atributos
'''
'''
Ahora con la siguiente clase corregida si puedes acceder a los métodos y modificarlos,
también con esto se puede ver la importancia del 'Self' en los métodos de las clases

class Casa:
    Rojo = False
    
    def __init__(self):
        print("Se crea una casa")

    def Fabricar(self):
        self.Rojo = True
    
    def confimar_fabricacion(self):
        if(self.Rojo):
            print("Casa color roja")
        else:
            print("Casa no pintada")

casa = Casa()
casa.confimar_fabricacion()
casa.Fabricar() #Con esto ya se puede modificar el atributo rojo de la clase con el método
print(casa.Rojo)
casa.confimar_fabricacion()
'''
'''
A continuación se mostrara otro ejemplo de uso del 'self' y del metodo '_init_'
class Auto:
    Rojo = False
    
    def __init__(self, puertas=None,color=None):
        self.puertas = puertas
        self.color = color
        if puertas is not None and color is not None:
            print("Se creo un auto de {} y color {}".format(puertas,color))
            
a = Auto()
b = Auto("4", "negro") #Se puede ver que solo se imprimio un msj, pues solo una instancia si cumplio con los parametros
'''

'''
A contincuación se verá más en profundidad sobre el método '_init_' que es un método constructor y ahora el método
destructor

class Fabrica:
    
    def __init__(self, tiempo, nombre, duenno):
        self.tiempo = tiempo
        self.nombre = nombre
        self.duenno = duenno
        print("Se creo la fabrica ", self.nombre)
        
    def __del__(self):
        print("Se elimino el auto", self.nombre)
        
a = Fabrica(10,"Hola",10)
b = Fabrica(10,"sonora", 10)
#Como se puede apreciar en la  terminal, se crea el objeto con el nombre y a la vez elimina el nombre, esto se debe a que
#en está ocasión se forma un bucle con  y el metodo desctructor '__del__' y, por lo tanto, solo puede existir un objeto
#instanciado, si se instania otro, se borra y se reemplaza con el nuevo objeto instanciado
'''
'''
A continuación se puede ver como se modifican los métodos por defecto de python con una instancia del objeto  de una clase
class Cadena:
    
    def __init__(self, tiempo, nombre, duenno):
        self.tiempo = tiempo
        self.nombre = nombre
        self.duenno = duenno
        print("Se creo la fabrica ", self.nombre)
        
    def __str__(self):
        return "{} se fabrico co exito, en el tiempo {} y su dueño es {}".format(self.nombre,self.tiempo,self.duenno)

    def __len__(self):
        return self.tiempo

a = Cadena(10, "Oxxo", "Luis")
print(str(a))
print(len(a))
'''
'''
Ahora se vera como se pueden usar dos clases y entralazarlas usando una lista y el método construtor

class Coche:
    def __init__(self,marca,duenno,puertas):
        self.marca = marca
        self.duenno = duenno
        self.puertas = puertas
        print("se creo el auto marca {}".format(self.marca))
    
    def __str__(self):
        return "marca: {} duenno: {} cantidad de puertas: {}".format(self.marca,self.duenno,self.puertas)

class Listado:
    listadoAutos = []
    
    def __init__(self, autos=[]):
        self.listadoAutos = autos
        
    def agregarAuto(self, objetoAuto):
        self.listadoAutos.append(objetoAuto)
        
    def visualizar(self):
        for iterador in self.listadoAutos:
            print(iterador)

a = Coche( "BMW", "Luis", 4)
l = Listado([a]) #Recuerda que estás recibiendo un argumento de tipo lista, así que envialo en ese formato
l.visualizar() #Ahora se puede acceder a los atributos de otra clase por el objeto y con el método alterado
#__str__ en la iteración del metodo visualizar
l.agregarAuto(Coche("Masseratti", "Jared", 2)) #Así se puede crear otro objeto dento de un método de otra clase
l.visualizar()
'''
'''
A conticuación se mostrará como se simula el encapsulamiento en python, puesto que en python no existe el
encapsulamiento como tal, y se tiene otra forma de encapsular los atributos e incluso los métodos
class Encapsulamiento:
    __privado_atributo ="Soy un atributo encapsulado"
    
    def __privado_metodo(self):
        print("Soy un método encapsulado")
        
a = Encapsulamiento()
a.__privado_atributo
a.__privado_metodo() #No importa cual de los dos intentes ejecutar, no se mostrará el mensaje a que están
#encapsulados o privados de modificaciones, para poder acceder a estos se usa lo siguiente
'''
class Encapsulamiento:
    __privado_atributo = "Sou un atributo privado"