class Calculadora():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a+self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b
    
    def imprimirOperaciones(self):
        print("Suma:",self.a,"+",self.b,"=",self.sumar())
        print("Resta:",self.a,"-",self.b,"=",self.restar())
        print("Multiplicación:",self.a,"*",self.b,"=",self.multiplicar())
        print("División:",self.a,"/",self.b,"=",self.dividir())

calculadora = Calculadora(10,5)
calculadora.imprimirOperaciones()

