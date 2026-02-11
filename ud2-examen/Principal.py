# AUTOR: ISRAEL BENJAMÍN GAGO ACUÑA
class Cliente():
    def __init__(self,dni,nombre,apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        
class Articulo():
    def __init__(self,codigo,denominacion,precio):
        self.codigo = codigo
        self.denominacion = denominacion
        self.precio = precio
        
class Factura():
    def __init__(self,numero,cliente,lineas):
        self.numero = numero
        self.cliente = cliente
        self.lineas = lineas
        
    def mostrarInformacion(self):
        precioTotal = 0
        print("Factura:",self.numero)
        print("Cliente:", self.cliente.nombre,self.cliente.apellidos,"-",self.cliente.dni)
        print("Articulos:")
        for articulo in self.lineas:
            print("Código:",articulo.codigo,"- Artículo",articulo.denominacion,"- Precio:",articulo.precio,"€")
            precioTotal+=articulo.precio
        print("Precio total:",precioTotal,"€")
        
cliente = Cliente("58392712B","Rosa","González")
lineas = [Articulo(1,"Televisor",399),
          Articulo(1,"Televisor",399),
          Articulo(2,"Tarjeta gráfica",239)]

factura = Factura(1,cliente,lineas)
factura.mostrarInformacion()