

import math

class Point:

    # _     veut dire protected attribut
    # __    veut dire private attribut
    #       veut dire public

    def __init__(self, abs: float = 0.0, ord: float = 0.0) -> None:
        self.__abs = abs
        self.__ord = ord

    @property
    def _abs(self):
        return self.__abs

    @_abs.setter
    def _abs(self, value):
        self.__abs = value

    @property
    def _ord(self):
        return self.__ord

    @_ord.setter
    def _ord(self, value):
        self.__ord = value

    @staticmethod
    def distance(x1,y1,x2,y2):
        return Point(x1,y1).calc_distance(x2,y2)

    def calc_distance(self,point:'Point')->float:
        return math.sqrt(math.pow(self._abs - point._abs, 2) + math.pow(self._ord - point._ord, 2));

    def calc_milieu(self,point):
        abs_m= (self.__abs + point._abs)/2
        ord_m= (self.__ord + point._ord)/2
        return Point(abs_m,ord_m);



    def __str__(self) -> str:
        return f'Object Point : {self.__abs} {self.__ord}'
