# Datos de ejemplo (pueden ser reemplazados por datos de entrada dinámicos)
maestros = [
    {'id_maestro': 1, 'nombre': 'm1', 'prioridad': 3, 'perfil': ['Algebra', 'Estadistica'], 'horas_disponibles': {'lunes': [(7, 9), (9, 11), (11, 13), (13, 15)], 'martes': [(8, 10), (10, 12), (12, 14), (14, 16)], 'miercoles': [(7, 9), (9, 11), (11, 13), (13, 15)], 'jueves': [(8, 10), (10, 12), (12, 14), (14, 16)], 'viernes': [(10, 12), (12, 14), (14, 16), (16, 18)]}},
    {'id_maestro': 2, 'nombre': 'm2', 'prioridad': 1, 'perfil': ['ingles 1', 'ingles 3'], 'horas_disponibles': {'lunes': [(7, 9), (9, 11)], 'martes': [(7, 11), (9, 11)], 'miercoles': [(8, 10), (10, 12)], 'jueves': [(8, 10), (10, 12)], 'viernes': [(7, 9), (9, 11)]}},
    {'id_maestro': 3, 'nombre': 'm3', 'prioridad': 3, 'perfil': ['Programacion 1'], 'horas_disponibles': {'lunes': [(7, 9), (9, 11), (11, 13), (13, 15)], 'martes': [(7, 9), (9, 11), (11, 13), (13, 15)], 'miercoles': [(7, 9), (9, 11), (11, 13), (13, 15)], 'jueves': [(7, 9), (9, 11), (11, 13), (13, 15)], 'viernes': [(7, 9), (9, 11), (11, 13), (13, 15)]}},
    {'id_maestro': 4, 'nombre': 'm4', 'prioridad': 2, 'perfil': ['Elaboración de textos', 'metodologia'], 'horas_disponibles': {'lunes': [(8, 10), (10, 12)], 'martes': [(8, 10), (10, 12)], 'miercoles': [(8, 10), (10, 12)], 'jueves': [(8, 10), (10, 12)], 'viernes': [(8, 10), (10, 12)]}},
    {'id_maestro': 5, 'nombre': 'm5', 'prioridad': 2, 'perfil': ['Fisica 1'], 'horas_disponibles': {'lunes': [(18, 20)], 'martes': [(18, 20)], 'miercoles': [(18, 20)], 'jueves': [(18, 20)], 'viernes': [(18, 20)]}}
]

materias = [
    {'id_materia': 1, 'id_grupo': 1, 'nombre': 'Programacion 1', 'horasPorSemana': 4},
    {'id_materia': 2, 'id_grupo': 1, 'nombre': 'ingles 1', 'horasPorSemana': 4},
    {'id_materia': 3, 'id_grupo': 1, 'nombre': 'Algebra', 'horasPorSemana': 6},
    {'id_materia': 4, 'id_grupo': 1, 'nombre': 'metodologia', 'horasPorSemana': 4},
    {'id_materia': 5, 'id_grupo': 1, 'nombre': 'Elaboración de textos', 'horasPorSemana': 4},
    {'id_materia': 6, 'id_grupo': 1, 'nombre': 'Introduccion a la ingenieria', 'horasPorSemana': 3},
    {'id_materia': 7, 'id_grupo': 1, 'nombre': 'Quimica', 'horasPorSemana': 4},
    {'id_materia': 8, 'id_grupo': 3, 'nombre': 'Estadistica', 'horasPorSemana': 6},
    {'id_materia': 9, 'id_grupo': 3, 'nombre': 'Sistemas Operativos', 'horasPorSemana': 4},
    {'id_materia': 10, 'id_grupo': 3, 'nombre': 'Calculo Vectorial', 'horasPorSemana': 6},
    {'id_materia': 11, 'id_grupo': 3, 'nombre': 'Logica Digital', 'horasPorSemana': 4},
    {'id_materia': 12, 'id_grupo': 3, 'nombre': 'Estructura de datos', 'horasPorSemana': 4},
    {'id_materia': 13, 'id_grupo': 3, 'nombre': 'Fisica 1', 'horasPorSemana': 6},
    {'id_materia': 14, 'id_grupo': 3, 'nombre': 'ingles 3', 'horasPorSemana': 4}
]

# Inicialización del horario del grupo y los maestros
horarios_grupos = {1: {dia: ['Libre' for _ in range(7, 19, 2)] for dia in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']},
                   3: {dia: ['Libre' for _ in range(7, 19, 2)] for dia in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']}}

horarios_maestros = {maestro['id_maestro']: {dia: ['Libre' for _ in range(7, 19, 2)] for dia in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']} for maestro in maestros}

# Función para asignar clases al horario del grupo y de los maestros
def asignar_clase(grupo, dia, hora_inicio, materia, maestro_id):
    # Asigna al horario del grupo
    indice = (hora_inicio - 7) // 2
    horarios_grupos[grupo][dia][indice] = f'{materia} ({maestro_id})'
    # Asigna al horario del maestro correspondiente
    horarios_maestros[maestro_id][dia][indice] = materia

# Generar los horarios de los grupos
for materia in materias:
    horas_restantes = materia['horasPorSemana']
    nombre_materia = materia['nombre']
    grupo = materia['id_grupo']
    
    # Encontrar al maestro que puede impartir esta materia
    maestro_info = next((m for m in maestros if nombre_materia in m['perfil']), None)
    if maestro_info is None:
        continue
    
    maestro_id = maestro_info['id_maestro']
    
    # Asignar horas disponibles respetando las restricciones
    for dia, horas in maestro_info['horas_disponibles'].items():
        # Verificar si la materia ya está asignada en este día
        if any(nombre_materia in clase for clase in horarios_grupos[grupo][dia]):
            continue  # Si la materia ya está asignada, saltar al siguiente día
        
        # Limitar a una asignación por día
        clases_asignadas_en_el_dia = 0
        
        for hora_inicio, hora_fin in horas:
            if clases_asignadas_en_el_dia >= 1:  # Limitar a una asignación por día
                break

            # Revisar que el bloque de tiempo esté libre tanto en el grupo como en el maestro
            bloque_libre_grupo = all(horario == 'Libre' for horario in horarios_grupos[grupo][dia][(hora_inicio - 7) // 2:(hora_fin - 7) // 2])
            bloque_libre_maestro = all(horario == 'Libre' for horario in horarios_maestros[maestro_id][dia][(hora_inicio - 7) // 2:(hora_fin - 7) // 2])
            
            # Verificar que las horas restantes de la materia puedan ser asignadas en este bloque de tiempo
            if horas_restantes > 0 and bloque_libre_grupo and bloque_libre_maestro:
                asignar_clase(grupo, dia, hora_inicio, nombre_materia, maestro_id)
                horas_restantes -= (hora_fin - hora_inicio)
                clases_asignadas_en_el_dia += 1
                
            # Salir si no quedan horas por asignar
            if horas_restantes <= 0:
                break
        if horas_restantes <= 0:
            break

# Mostrar el horario de cada grupo
for grupo, horario in horarios_grupos.items():
    print(f"\nHorario del Grupo {grupo}:")
    for dia, horarios in horario.items():
        print(f"{dia.capitalize()}: {', '.join(horarios)}")

# Mostrar el horario de cada maestro
print("\nHorarios de los Maestros:")
for maestro_id, horarios in horarios_maestros.items():
    print(f"\nMaestro {maestro_id}:")
    for dia, horario in horarios.items():
        print(f"{dia.capitalize()}: {', '.join(horario)}")
