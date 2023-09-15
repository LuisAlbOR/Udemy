
class Universidad():
    def __init__(self, Nombre) -> None:
        self.nombreUni = Nombre
        
class Carrera():
    def Carrera(self,Carrera):
        self.Carrera = Carrera
        
class Estudiante(Universidad,Carrera):
    def datos(self,nombreEst,EdadEst):
        self.nombreEst = nombreEst
        self.EdadEst = EdadEst
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}. "
              "Estudio en la universidad {}".format(self.nombreEst,self.EdadEst,self.Carrera,self.nombreUni))
              
persona = Estudiante("Unach")
persona.Carrera("Software")
persona.datos("Luis",20)