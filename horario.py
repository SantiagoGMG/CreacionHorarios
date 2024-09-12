import random

class Maestro:
    def __init__(self, nombre, prioridad, horas_disponibles, materias):
        self.nombre = nombre
        self.prioridad = prioridad
        self.horas_disponibles = horas_disponibles
        self.materias = materias

class Materia:
    def __init__(self, nombre, duracion, maestro):
        self.nombre = nombre
        self.duracion = duracion
        self.maestro = maestro

# Inicializamos los maestros y sus horarios
maestros = [
    Maestro("Base de datos", 4, [5, 6], ["Base de datos"]),
    Maestro("Inglés", 1, [0, 1], ["Inglés"]),
    Maestro("Programación Avanzada", 5, [2, 3], ["Programación Avanzada"]),
    Maestro("Diseño Web", 5, [4, 5], ["Diseño Web"]),
    Maestro("Sistemas embebidos", 5, [6, 7], ["Sistemas embebidos"]),
    Maestro("Redes de computadoras", 5, [0, 1], ["Redes de computadoras"]),
    Maestro("Concurrencia y paralelismo", 5, [2, 3], ["Concurrencia y paralelismo"])
]

# Inicializamos el horario vacío
horario = [[None for _ in range(8)] for _ in range(5)]

def es_valido(dia, hora, materia):
    if hora + materia.duracion > 8:
        return False

    for i in range(materia.duracion):
        if horario[dia][hora + i] is not None:
            return False

    return True

def asignar_horario(materias, dia=0, hora=0):
    if not materias:
        return True
    
    if dia >= 5:
        return False

    if hora >= 8:
        return asignar_horario(materias, dia + 1, 0)

    materia_actual = materias[0]

    for h in range(hora, 8 - materia_actual.duracion + 1):
        if es_valido(dia, h, materia_actual):
            for i in range(materia_actual.duracion):
                horario[dia][h + i] = materia_actual

            if asignar_horario(materias[1:], dia, h + materia_actual.duracion):
                return True

            for i in range(materia_actual.duracion):
                horario[dia][h + i] = None

    return asignar_horario(materias, dia + 1, 0)

def llenar_horarios():
    global horario
    for _ in range(100):  # Intenta varias veces para llenar todos los días
        horario = [[None for _ in range(8)] for _ in range(5)]  # Reiniciar horario
        random.shuffle(materias)  # Barajar materias para variedad
        if asignar_horario(materias):
            return True
    return False

# Ejemplo de materias
materias = [
    Materia("Base de datos", 2, maestros[0]),
    Materia("Inglés", 2, maestros[1]),
    Materia("Programación Avanzada", 2, maestros[2]),
    Materia("Diseño Web", 2, maestros[3]),
    Materia("Sistemas embebidos", 2, maestros[4]),
    Materia("Redes de computadoras", 2, maestros[5]),
    Materia("Concurrencia y paralelismo", 2, maestros[6]),
    Materia("Concurrencia y paralelismo", 2, maestros[6])
]

if llenar_horarios():
    print("Se asignaron todos los horarios:")
    for dia in range(5):
        print(f"Día {dia+1}: {[(materia.nombre if materia else None) for materia in horario[dia]]}")
else:
    print("No se pudo encontrar una solución.")
