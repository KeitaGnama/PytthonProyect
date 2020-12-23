#constructor o inicializador nos serve inicializar los objetos de forma predeterminada

class Persona:
    nBrazos=0
    nPiernas=0
    cabello=True
    cCabello="Defecto"
    hambre=0

    #inicializador
    def __init__(self):
        self.nBrazos=2
        self.nPiernas=2

#metodos y dentro del parentesis coloquemos los atributos
    def dormir():
        pass
    def comer(self):
        self.hambre=0        
        
class Hombre:
    nombre="Defecto"
    sexo="M"
    #metodo
    def cambiarNombre(self,nombre):
        self.nombre=nombre

class Mujer:
    nombre="Defecto"
    sexo="F"