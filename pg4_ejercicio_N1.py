# Ejercicio 1

notas = [[], [], []]


def ingresar_notas():
    for i in range(3):
        print(f"Ingrese las notas finales para el curso {i+1}:")
        for j in range(5):
            nota = float(input(f"Nota del estudiante {j+1}: "))
            notas[i].append(nota)


def calcular_promedio_grupo(curso):
    return sum(notas[curso]) / len(notas[curso])


def calcular_porcentaje_aprobados(curso):
    aprobados = sum(1 for nota in notas[curso] if nota >= 70)
    return (aprobados / len(notas[curso])) * 100


def encontrar_max_min(curso):
    max_nota = max(notas[curso])
    min_nota = min(notas[curso])
    return max_nota, min_nota


ingresar_notas()

promedio_total = sum(sum(curso) for curso in notas) / sum(len(curso) for curso in notas)
print(f"El promedio total de todos los estudiantes es: {promedio_total}")

for i in range(3):
    promedio_grupo = calcular_promedio_grupo(i)
    print(f"Promedio del curso {i+1}: {promedio_grupo}")

for i in range(3):
    porcentaje_aprobados = calcular_porcentaje_aprobados(i)
    print(f"Porcentaje de aprobados en el curso {i+1}: {porcentaje_aprobados}%")

for i in range(3):
    max_nota, min_nota = encontrar_max_min(i)
    print(f"Nota mayor en el curso {i+1}: {max_nota}")
    print(f"Nota menor en el curso {i+1}: {min_nota}")




#ejercicio 2

pasajeros = [[0 for _ in range(4)] for _ in range(5)]

def capturar_pasajeros():
    for i in range(5):
        for j in range(4):
            while True:
                p = int(input(f"Ingrese la cantidad de pasajeros del servicio {j+1} del día {i+1}: "))
                if 0 <= p <= 60:
                    pasajeros[i][j] = p
                    break
                else:
                    print("La cantidad de pasajeros debe ser un número entre 0 y 60. Intente de nuevo.")

def promedio_por_dia():
    return [sum(pasajeros[i]) / 4 for i in range(5)]

def promedio_general():
    return sum(sum(pasajeros[i]) for i in range(5)) / 20

def mejor_servicio():
    servicios = [sum(pasajeros[i][j] for i in range(5)) for j in range(4)]
    return servicios.index(max(servicios)) + 1

def momento_menos_pasajeros():
    dia = min(range(5), key=lambda i: min(pasajeros[i]))
    servicio = pasajeros[dia].index(min(pasajeros[dia]))
    return dia + 1, servicio + 1

def menu():
    while True:
        print("1. Capturar pasajeros")
        print("2. Mostrar promedio por día")
        print("3. Mostrar promedio general")
        print("4. Mostrar el mejor servicio")
        print("5. Mostrar el momento con menos pasajeros")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            capturar_pasajeros()
        elif opcion == 2:
            print(f"Promedio por día: {promedio_por_dia()}")
        elif opcion == 3:
            print(f"Promedio general: {promedio_general()}")
        elif opcion == 4:
            print(f"El mejor servicio es el servicio {mejor_servicio()}")
        elif opcion == 5:
            dia, servicio = momento_menos_pasajeros()
            print(f"El momento con menos pasajeros es el servicio {servicio} del día {dia}")
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
