# Solicita 8 calificaciones y calcula el promedio
calificaciones = []
for i in range(8):
    cal = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(cal)

promedio = sum(calificaciones) / len(calificaciones)
print("El promedio es:", promedio)
