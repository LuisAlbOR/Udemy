class Primera:
    def __init__(self):
        print("Soy la primera clase")
    
    def primera(self):
        print("Este es el método heredado de primera")
    
class Segunda:
    def __init__(self):
        print("Soy la segunda")
        
    def segunda(self):
        print("Este es el método heredado de segunda")
        
class Tercera (Segunda, Primera):
        
    def tercera(self):
        print("Este el metodo heredado de tercera")
        
herencia_multiple = Tercera()

herencia_multiple.tercera()
herencia_multiple.primera()
herencia_multiple.segunda() #Así se prueba la herencia multiple en python