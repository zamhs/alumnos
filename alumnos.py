# Crear una lista vacía para almacenar los datos de los alumnos
alumnos = []

# Preguntar cuántos alumnos se van a ingresar
cantidad_alumnos = int(input("¿Cuántos alumnos desea ingresar? "))

# Recoger los datos de los alumnos
for i in range(cantidad_alumnos):
    print(f"\nIngrese los datos del alumno {i+1}:")
    matricula = input("Matrícula: ")
    apellidos = input("Apellidos: ")
    nombres = input("Nombres: ")
    promedio = float(input("Promedio final: "))
    
    # Crear un diccionario con los datos del alumno
    alumno = {
        "matrícula": matricula,
        "apellidos": apellidos,
        "nombres": nombres,
        "promedio": promedio
    }
    
    # Añadir el diccionario del alumno a la lista de alumnos
    alumnos.append(alumno)

# Encontrar el mayor promedio
mayor_promedio = max(alumno["promedio"] for alumno in alumnos)

# Crear una lista para los alumnos con el mayor promedio
mejores_alumnos = []

# Filtrar los alumnos con el mayor promedio
for alumno in alumnos:
    if alumno["promedio"] == mayor_promedio:
        mejores_alumnos.append(alumno)

# Mostrar los datos de los alumnos con el mayor promedio
print("\nAlumnos con el mayor promedio:")
for alumno in mejores_alumnos:
    print(f"Matrícula: {alumno['matrícula']}, Apellidos: {alumno['apellidos']}, Nombres: {alumno['nombres']}, Promedio: {alumno['promedio']}")
