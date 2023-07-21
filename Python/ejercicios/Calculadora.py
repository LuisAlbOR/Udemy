class Calculadora:
    
    def __init__(self):
        self.numeroUno = float(input("Ingrese un numero... "))
        self.numeroDos = float(input("Ingrese otro numero... "))
        self.suma()
        self.resta()
        self.multi()
        self.division()
        
    def suma(self) -> None:
        print("Suma: {}".format(self.numeroUno+self.numeroDos))
        
    def resta(self) -> None:
        print("Resta: {}".format(self.numeroUno-self.numeroDos))
        
    def multi(self) -> None:
        print("Multiplicación: {}".format(self.numeroUno*self.numeroDos))
        
    def division(self) -> None:
        print("División: {}".format(self.numeroUno/self.numeroDos))
        
calculadora = Calculadora()