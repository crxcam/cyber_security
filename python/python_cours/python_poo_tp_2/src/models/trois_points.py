from __future__ import annotations

from src.models.point import Point


def check_sont_aligne(value1, value2, value3) -> bool:
    return value1 == (value2+value3)


class TroisPoints:

    def __init__(self, une: Point, deux: Point, trois: Point) -> None:
        self.__une = une
        self.__deux = deux
        self.__trois = trois

    @property
    def _une(self):
        return self.__une

    @_une.setter
    def _une(self, value):
        self.__une = value

    @property
    def _deux(self):
        return self.__deux

    @_deux.setter
    def _deux(self, value):
        self.__deux = value

    @property
    def _trois(self):
        return self.__trois

    @_trois.setter
    def _trois(self, value):
        self.__trois = value

    def sont_alignes(self) -> bool:
        ab = self._une.calc_distance(self._deux)
        ac = self._une.calc_distance(self._trois)
        bc = self._deux.calc_distance(self._trois)
        test = False
        if check_sont_aligne(ab, ac, bc):
            test = True
        elif check_sont_aligne(ac, ab, bc):
            test = True

        elif check_sont_aligne(ac, ab, bc):
            test = True
        
        return test

