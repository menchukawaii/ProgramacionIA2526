import math

#hypot() calcula la distancia entre 2 puntos

class Point:

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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
