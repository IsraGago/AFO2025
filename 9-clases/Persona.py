class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("edad:",self.edad)
        self.mostrarEsMayorEdad()

    def mostrarEsMayorEdad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")

persona = Persona("Israel",21)
persona.imprimir()