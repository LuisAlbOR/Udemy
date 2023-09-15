
class Marino():
    def hablar(self):
        print("hola...")
        
class Pulpo(Marino):
    def hablar(self):
        print("Soy un pulpo")
        
class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Soy una foca")