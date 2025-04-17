"""
Ejercicio 3
 Se necesita elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco,
 correspondientes a un postulante, y muestre su puntaje final considerando que por cada respuesta correcta
  tendrá 3 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.
"""

correctas = int(input("Ingrese la cantidad de respuestas correctas: "))
incorrectas = int(input("Ingrese la cantidad de respuestas incorrectas: "))
en_blanco = int(input("Ingrese la cantidad de respuestas en blanco: "))

puntaje = (correctas * 3) + (incorrectas * -1) + (en_blanco * 0)
porcentaje = puntaje / ((correctas + incorrectas + en_blanco) * 3)*100

print(f"El puntaje final del postulante es: {puntaje}")
print(f"El porcentaje final del postulante es: {porcentaje:.2f}%")