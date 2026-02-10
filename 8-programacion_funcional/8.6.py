"""
Escribir una función reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva otro diccionario con las 
asignaturas en mayúsculas y las calificaciones correspondientes 
a las notas. 
"""

def obtener_calificacion(nota):
    """Convierte una nota numérica en una palabra descriptiva."""
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    elif nota < 10:
        return "Sobresaliente"
    else:
        return "Matrícula de Honor"

def procesar_notas(asignaturas):
    """
    Transforma un diccionario de notas:
    - Claves a MAYÚSCULAS.
    - Notas a Calificaciones (texto).
    """
    # Usamos comprensión de diccionarios para transformar ambos campos
    return {nombre.upper(): obtener_calificacion(nota) 
            for nombre, nota in asignaturas.items()}

# --- Ejemplo de uso ---
notas_alumno = {
    "Matemáticas": 9.5,
    "Física": 4.8,
    "Programación": 7.2,
    "Historia": 6.0
}

resultado = procesar_notas(notas_alumno)

print("Diccionario procesado:")
for asignatura, calificacion in resultado.items():
    print(f"{asignatura}: {calificacion}")