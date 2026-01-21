class Tarjeta():
        numero = 35331256
        banco = "Santander"

        def imprimir(self):
                print("Número de tarjeta: " + str(self.numero))
                print("Banco "+self.banco)

        def __init__(self,numero,banco):
                self.numero = numero
                self.banco = banco

tl = Tarjeta(54321342,"Abanca")
tl.imprimir()