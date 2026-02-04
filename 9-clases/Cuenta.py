class Cuenta():
    def __init__(self,titular: str,cantidad: float):
        self.titular = titular
        self.cantidad = cantidad
    
    def imprimir_datos(self):
        print("titular:",self.titular,",cantidad:",self.cantidad)
        
class CajaAhorro(Cuenta):
    def __init__(self,titular: str,cantidad: float):
        super().__init__(titular,cantidad)
        
class PlazoFijo(Cuenta):
    def __init__(self, titular: str, cantidad: float,plazo: int,interes:float):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def get_importe_interes(self):
        return self.cantidad * self.interes / 100
    
    def imprimir_datos(self):
        super().imprimir_datos()
        print("plazo:",self.plazo)
        print("interes:",self.interes)
        print("importe interes:",self.get_importe_interes())

cuentas: list[Cuenta] = [CajaAhorro("Israel Gago",15000),
           PlazoFijo("Rode Sánchez",20000,12,5),]  
for cuenta in cuentas:
    cuenta.imprimir_datos()
    print("-----")