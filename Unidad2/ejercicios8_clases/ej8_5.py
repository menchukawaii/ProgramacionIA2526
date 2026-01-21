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


class Triangle:

    def __init__(self, puntoA, puntoB, puntoC):
        self.__puntoA = puntoA
        self.__puntoB = puntoB
        self.__puntoC = puntoC


    def perimeter(self):
        distancia_a_b = self.__puntoA.distance_from_point(self.__puntoB)
        distancia_b_c = self.__puntoB.distance_from_point(self.__puntoC)
        distancia_c_a = self.__puntoC.distance_from_point(self.__puntoA)
        return distancia_a_b + distancia_b_c + distancia_c_a



triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
