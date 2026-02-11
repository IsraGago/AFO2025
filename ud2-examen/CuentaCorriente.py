# AUTOR: ISRAEL BENJAMÍN GAGO ACUÑA
class CuentaCorriente():
    def __init__(self,nombre,apellido,direccion,telefono,nif,saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.nif = nif
        self.saldo = saldo
    
    def retirarDinero(self,cantidadRetirada):
        self.saldo -= cantidadRetirada
        
    def ingresarDinero(self,cantidadIngresada):
        if cantidadIngresada > 0:
           self.saldo += cantidadIngresada
        
    def consultarCuenta(self):
        print("Titular:",self.nombre,self.apellido)
        print("Dirección:",self.direccion)
        print("Telefono:",self.telefono)
        print("NIF:",self.nif)
        print("Saldo:",self.saldo)
        
    def saldoNegativo(self):
        return self.saldo < 0
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getApellido(self):
        return self.apellido
    
    def setApellido(self,apellido):
        self.apellido = apellido

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self,direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self,telefono):
        self.telefono = telefono

    def getNIF(self):
        return self.nif
    
    def setNIF(self,nif):
        self.nif = nif

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self,saldo):
        self.saldo = saldo

    
cuenta1 = CuentaCorriente("Israel","Gago","Dr Otero Ulloa 100","688392044","84372832P",1000)
cuenta1.ingresarDinero(10)
cuenta1.retirarDinero(1100)
cuenta1.consultarCuenta()

if cuenta1.saldoNegativo():
    print("La cuenta tiene saldo negativo")
else:
    print("La cuenta tiene saldo positivo")