def datos_personales(nombre,edad,ciudad = "Pontevedra"):
    print("Me llamo " + nombre)
    print("Mi edad es",edad)
    print("Vivo en " + ciudad)
datos_personales("Israel",21)
datos_personales("Benjamín",22,"Marín")

def nombreCompleto(**datos):
    print(type(datos))
    print("Datos completos: "+datos["nombre"],datos["apellido"])

nombreCompleto(nombre = "Israel",apellido="Gago")
