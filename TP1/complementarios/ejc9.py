"""
Ejercicio 9
Determinar si el alumno está Promocionado (nota mayor o igual a 80),
 Regular (nota mayor o igual a 60 PERO menor que 80) o Desaprobado (nota menor a 60)
"""
nota = float(input("Ingrese la nota del alumno (de 0 a 100): "))

if nota >= 80:
    print("Estado: Promocionado")
elif nota >= 60:
    print("Estado: Regular")
else:
    print("Estado: Desaprobado")