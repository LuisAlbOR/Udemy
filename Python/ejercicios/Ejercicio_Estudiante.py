class Estudiante:
    
    def Datos(self, nombreEstudiante, notaEstudiante) -> None:
        self.nombreEstudiante = nombreEstudiante
        self.notaEstudiante = notaEstudiante
    
    def ImprimirDatos(self) -> None:
        print("Nombre: {}, Calificación {}".format(self.nombreEstudiante,self.notaEstudiante))
    
    def ImprimirDecision(self) -> None:
        if self.VerificarNotaAprobatoria(self.notaEstudiante):
            print("Nota aprobatoria")
        else:
            print("Nota no aprobatoria")

    def VerificarNotaAprobatoria(self, notaEstudiante) -> bool:
        if notaEstudiante > 5:
            return True
        

alumnoUno = Estudiante()
alumnoUno.Datos("Juan", 5)
alumnoUno.ImprimirDatos()
alumnoUno.ImprimirDecision()