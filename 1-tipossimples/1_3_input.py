nombre = input("Dime un nombre: ")
print("¡Hola",nombre+"!")

edad = int(input("Dime tu edad: "))

#Concatenando con comas no hace falta castear a string
print("El año que viene tendrás",edad+1,"años.")

#Concatenando con "+" si hace falta castear a string
print("El año que viene tendrás "+str(edad+1)+" años.")
