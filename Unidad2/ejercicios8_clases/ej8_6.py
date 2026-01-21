import math


class Point:
    # ejercicio 8.2
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x


    def gety(self):
        return self.__y


    def distance_from_xy(self, a, b):   
        diff_x = self.__x - a
        diff_y = self.__y - b
        # math.hypot calcula la raíz cuadrada de la suma de los cuadrados
        return math.hypot(diff_x, diff_y)


    def distance_from_point(self, point):
        diff_x = self.__x - point.getx()
        diff_y = self.__y - point.gety()
        return math.hypot(diff_x, diff_y)


class Polygon:
    def __init__(self, *vertices):
        self.__vertices = list(vertices) #convierte la tupla a una lista

    def perimeter(self):
        perimetro = 0
        for i in range(len(self.__vertices)):
            if i < (len(self.__vertices) -1):
                perimetro += self.__vertices[i].distance_from_point(self.__vertices[i + 1])
            else:
                perimetro += self.__vertices[i].distance_from_point(self.__vertices[0])
        return perimetro
        


poligono = Polygon(Point(0, 0), Point(1, 0), Point(0, 1))

print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(1, 0), Point(1,1), Point(0, 1))

print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(2, 0), Point(2,1), Point(0, 1))

print(poligono.perimeter())

poligono = Polygon(Point(0, 0), Point(2, 0), Point(1,1), Point(0, 1))

print(poligono.perimeter())
