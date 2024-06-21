
from  __future__  import annotations
from typing import List



class ListePersonnes:

    def __init__(self, personnes: List[Personne] | None=None) -> None:
        self.__personnes = personnes

    @property
    def _personnes(self):
        return self.__personnes

    @_personnes.setter
    def _personnes(self, value):
        self.__personnes = value
