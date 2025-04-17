'''
Ejercicio 1 
Crear una función que calcule y retorne el área de un  triángulo, recibe la base y altura 
'''

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

print(calcular_area_triangulo(10, 5))
print(calcular_area_triangulo(3, 4))