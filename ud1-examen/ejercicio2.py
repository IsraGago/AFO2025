# AUTOR: ISRAEL BENJAMÍN GAGO ACUÑA
agenda = {}
print("AGENDA")

def imprimirMenu():
    print("1 - Añadir/modificar")
    print("2 - Buscar")
    print("3 - Borrar")
    print("4 - Listar")
    print("0 - Salir")

while(True):
    imprimirMenu()
    respuesta = input("Introduce el número de la opción deseada: ")

    if respuesta == "0": # SALIR
        break
    elif respuesta == "1": # AÑADIR / MODIFICAR
        nombre = input("Introduce un nómbre: ")
        if nombre in agenda:
            print("el nombre existe en la agenda con el número: ", agenda[nombre])
            respuesta = input("desea modificar el número asociado (s/n): ")
            if respuesta.lower() == "s":
                numero = input("introduce un número: ")
                agenda[nombre] = numero
                print("Contacto modificado exitosamente.")
            elif respuesta.lower() == "n":
                print("Operación cancelada.")
        else:
            print("El contacto no existe.")
            numero = input("introduce su número: ")
            agenda[nombre] = numero
            print("Contacto introducido con éxito.")
    elif respuesta == "2": # BUSCAR
        filtro = input("Introduce el filtro: ")
        for nombreContacto,numero in agenda.items():
            if filtro == nombreContacto[0:len(filtro)]:
                print(nombreContacto,":",numero)
    elif respuesta == "3": # ELIMINAR
        nombre = input("Introduce un nombre: ")
        if nombre in agenda:
            agenda.pop(nombre)
            print("Contacto borrado exitosamente.")
        else:
            print("No existe un contacto con el nombre",nombre+".")
    elif respuesta == "4": # LISTAR TODOS
        if len(agenda) == 0:
            print("No hay contactos.")
        else:
            for nombreContacto,numero in agenda.items():
                print(nombreContacto,":",numero)
    print("")
print("Cerrando programa.")


