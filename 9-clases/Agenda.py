class Persona():
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda():
    def __init__(self,listaPersonas):
        self.listaPersonas = listaPersonas

    # def addContacto(self,persona):
        # self.persona