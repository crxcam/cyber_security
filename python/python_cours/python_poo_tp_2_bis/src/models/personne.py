

from enum import Enum
from typing import List

from src.models.address import Address



class Sex(Enum):
    M = 'M'
    F = 'F'


class Personne:
    def __init__(self,  nom: str = '', sex: Sex = Sex.M, adresses: List[Address] | None =None) -> None:
        self.__nom = nom
        self.__sex = sex
        self.__adresses = adresses

    @property
    def _nom(self):
        return self.__nom

    @_nom.setter
    def _nom(self, value):
        self.__nom = value

    @property
    def _sex(self):
        return self.__sex

    @_sex.setter
    def _sex(self, value):
        self.__sex = value

    @property
    def _adresses(self):
        return self.__adresses

    @_adresses.setter
    def _adresses(self, value):
        self.__adresses = value


    def __str__(self) -> str:
        return f' nom:{self._nom} sex:{self._sex}'
