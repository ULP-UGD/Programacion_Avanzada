"""
Ejercicio 1 
Crear una clase Guerrero que sea reciba como atributos: 
● Nombre del guerrero. 
● Vida del guerrero. 
● Ataque del guerrero. 
● Arma. 
Como métodos deberá tener: 
● __str__. 
● Atacar. 
● Mejorar arma. (Deberá mejorar la categoría del arma) 
El atributo Arma será otra clase que tendrá los siguientes atributos: 
● Tipo de arma. 
● Ataque del arma. 
● Categoria del arma. 
y la clase Arma tendrá los siguientes métodos: 
● __str__. 
● Mejorar categoria. (Deberá aumentar el daño del arma) 
Una vez creadas ambas clases, deberá crear dos guerreros, uno será “John Snow” y el 
otro será un “caminante blanco” y deberá hacer que “John Snow” ataqué al caminante 
blanco. 
"""
class Arma:
    def __init__(self, tipo: str, ataque: int, categoria: int = 1):
        self.tipo = tipo
        self.ataque = ataque
        self.categoria = categoria
    
    def __str__(self):
        return f"Arma {self.tipo} (Ataque: {self.ataque}, Categoría: {self.categoria})"
    
    def mejorar_categoria(self):
        self.categoria += 1
        self.ataque += 5  
        return self

class Guerrero:
    def __init__(self, nombre: str, vida: int, ataque: int, arma: Arma):
        self.nombre = nombre
        self.vida = vida
        self.ataque_base = ataque
        self.arma = arma
    
    def __str__(self):
        return f"{self.nombre} (Vida: {self.vida}, Ataque total: {self.ataque_total()}) - {self.arma}"
    
    def ataque_total(self):
        return self.ataque_base + self.arma.ataque
    
    def atacar(self, otro_guerrero):
        danio = self.ataque_total()
        otro_guerrero.vida -= danio
        print(f"{self.nombre} ataca a {otro_guerrero.nombre} causando {danio} de daño!")
    
    def mejorar_arma(self):
        self.arma.mejorar_categoria()
        print(f"¡{self.nombre} ha mejorado su {self.arma.tipo} a categoría {self.arma.categoria}!")
        return self

# Crea de los guerreros
espada_larga = Arma("Espada larga", 15)
daga_hielo = Arma("Daga de hielo", 20, 2)

john_snow = Guerrero("John Snow", 100, 30, espada_larga)
caminante_blanco = Guerrero("Caminante Blanco", 120, 25, daga_hielo)

# Simula el ataque
print("Antes del ataque:")
print(john_snow)
print(caminante_blanco)
print()

john_snow.atacar(caminante_blanco)
print()

print("Después del ataque:")
print(john_snow)
print(caminante_blanco)
print()

# Mejora el arma
john_snow.mejorar_arma()
print(john_snow)