
from typing import Optional



class Personne:
    def __init__(self, num: int = 0, nom: str = '', prenom: str = '') -> None:
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom

    @property
    def _num(self):
        return self.__num

    @_num.setter
    def _num(self, value):
        self.__num = value

    @property
    def _nom(self):
        return self.__nom

    @_nom.setter
    def _nom(self, value):
        self.__nom = value

    @property
    def _prenom(self):
        return self.__prenom

    @_prenom.setter
    def _prenom(self, value):
        self.__prenom = value


    




 

# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f' id:{self._num} nom:{self._nom} prenom:{self._prenom}'

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
