import math

class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def imprimir_detalles(self):
        # Este es el método concreto que aprovecha el polimorfismo
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")
        print("-" * 20)
    

class Circle(FiguraGeometrica):
    def __init__(self, radio):
        self.__radio = radio
    
    def calcular_area(self):
        return math.pi * (self.__radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio
    
class Rectangle(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    def calcular_area(self):
        return self.__ancho * self.__alto
    
    def calcular_perimetro(self):
        return 2 * (self.__ancho + self.__alto)

class Triangle(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    
    def calcular_area(self):
        return (self.__base * self.__altura) / 2
    
    def calcular_perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3
    


def imprimir_detalles(self):
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Área: {self.calcular_area():.2f}") # :.2f formatea a 2 decimales
        print(f"Perímetro: {self.calcular_perimetro():.2f}")
        print("-" * 20)