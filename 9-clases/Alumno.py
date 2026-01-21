class Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
        self.mostrarAprobado()

    def mostrarAprobado(self):
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("Suspenso")

alumno = Alumno("Israel",7)
alumno.imprimir()
