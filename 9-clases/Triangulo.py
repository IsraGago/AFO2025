class Triangulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def imprimir_lado_mayor(self):
        mayor = 0
        letra = "z"
        if self.a > mayor:
            letra = "a"
            mayor = self.a
        if self.b > mayor:
            letra = "b"
            mayor = self.b
        if self.c > mayor:
            letra  ="c"
            mayor = self.c
        
        print("El lado mayor es el",letra+":",mayor)
    
    def imprimir_tipo(self):
        if self.a == self.b and self.b == self.c:
            print("Equilátero")
        elif self.a != self.b and self.b != self.c and self.a != self.c:
            print("Escaleno")
        #elif (self.a == self.b and self.a != self.c) or (self.b == self.c and self.b != self.a):
        else:
            print("Isosceles")

    def imprimir_valores(self):
        print("lado A:",self.a) 
        print("lado B:",self.b) 
        print("lado C:",self.c) 

t = Triangulo(5,4,6)
t.imprimir_valores()
t.imprimir_lado_mayor()
t.imprimir_tipo()