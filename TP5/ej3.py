"""
Ejercicio 3 
Extiende el programa anterior que implementa figuras geométricas con los siguientes 
requisitos: 
Clase FiguraBidimensional: Crea una nueva clase llamada FiguraBidimensional que Esta 
clase debe contener un método clonar(self) que devuelve una copia de la instancia (puedes 
usar copy para realizar la clonación). 
Clase FiguraTridimensional: Crea una clase diferente llamada FiguraTridimensional, que 
debe incluir un método calcular_volumen(self) que deberá ser implementado por las clases 
derivadas que representen figuras tridimensionales. 
Crear la clase Derivada Cubo: Crea una nueva clase llamada Cubo que derive de 
FiguraGeometrica FiguraBidimensional, FiguraTridimensional. Esta clase debe tener un 
constructor que acepte el lado del cubo. 
Modificar la clase Circulo para que herede ahora también de FiguraBidimensional.
"""
import copy
from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        pass

class FiguraBidimensional:
    def clonar(self):
        return copy.deepcopy(self)

class FiguraTridimensional(ABC):
    @abstractmethod
    def calcular_volumen(self) -> float:
        pass

class Circulo(FiguraGeometrica, FiguraBidimensional):
    def __init__(self, radio: float):
        self.radio = radio
    
    def area(self) -> float:
        return math.pi * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Círculo (radio={self.radio})"

class Cubo(FiguraGeometrica, FiguraBidimensional, FiguraTridimensional):
    def __init__(self, lado: float):
        self.lado = lado
    
    def area(self) -> float:
        return 6 * self.lado ** 2
    
    def perimetro(self) -> float:
        return 12 * self.lado
    
    def calcular_volumen(self) -> float:
        return self.lado ** 3
    
    def __str__(self):
        return f"Cubo (lado={self.lado})"

# Demostración del funcionamiento
circulo = Circulo(5)
copia_circulo = circulo.clonar()

cubo = Cubo(3)

print("Original:", circulo)
print("Clon:", copia_circulo)
print()

print("Cubo:")
print(f"Área: {cubo.area():.2f}")
print(f"Perímetro: {cubo.perimetro():.2f}")
print(f"Volumen: {cubo.calcular_volumen():.2f}")