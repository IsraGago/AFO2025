class Persona():
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda():
    def __init__(self):
        self.listaPersonas = []

    def addContacto(self,persona: Persona):
        self.listaPersonas.append(persona)
        print(persona.nombre + " ha sido añadido a la agenda.")
        return True
        
    def listarContactos(self):
        print("Contactos en la agenda:")
        for persona in self.listaPersonas:
            print("Nombre: " + persona.nombre + ", Teléfono: " + persona.telefono + ", Email: " + persona.email)
            
    def buscarContacto(self,nombre):
        for persona in self.listaPersonas:
            if persona.nombre == nombre:
                print("Contacto encontrado: Nombre: " + persona.nombre + ", Teléfono: " + persona.telefono + ", Email: " + persona.email)
                
            
    def editarContacto(self,nombre, nuevo_telefono, nuevo_email):
        for persona in self.listaPersonas:
            if persona.nombre == nombre:
                persona.telefono = nuevo_telefono
                persona.email = nuevo_email
                print("Contacto actualizado: Nombre: " + persona.nombre + ", Teléfono: " + persona.telefono + ", Email: " + persona.email)
                return

def mostrar_menu():
    print("\nAGENDA DE CONTACTOS")
    print("1.- Añadir contacto")
    print("2.- Listar contactos")
    print("3.- Buscar contacto")
    print("4.- Editar contacto")
    print("0.- Salir")
    
def agregar_contacto():
    print("AÑADIR CONTACTO")
    nombre = input("Introduzca el nombre: ")
    numero = input("Introduzca el número: ")
    email = input("Introduzca el email: ")
    p = Persona(nombre,numero,email)
    if agenda.addContacto(p):
        print("Contacto añadido correctamente.")
    else:
        print("Error el contacto ya existe.")

def buscar_contacto():
    print("\nBuscar contacto\n")
    nombre = input("Introduzca el nombre del contacto a buscar: ")
    agenda.buscarContacto(nombre) 

def editar_contacto():
    print("\nEditar contacto\n")
    nombre = input("Introduzca el nombre del contacto a editar: ")
    nuevo_telefono = input("Introduzca el nuevo número de teléfono: ")
    nuevo_email = input("Introduzca el nuevo email: ")
    agenda.editarContacto(nombre, nuevo_telefono, nuevo_email)  
            
agenda  = Agenda()
persona = Persona("Israel Gago","622095700","isragagoacuna@gmail.com")
agenda.addContacto(persona)


salir = False;
while not salir:
    mostrar_menu()
    match input("Selecciona una opción: "):
        case "1":
            agregar_contacto()
        case "2":
            agenda.listarContactos()
        case "3":
            buscar_contacto()         
        case "4":
            editar_contacto()
            
        case "0":
            salir = True
            print("Saliendo de la agenda...")
    