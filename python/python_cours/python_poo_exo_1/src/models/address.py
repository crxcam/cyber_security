
from  __future__  import annotations
from typing import Optional

class Address:

    # _     veut dire protected attribut
    # __    veut dire private attribut
    #       veut dire public

    def __init__(self, rue: str = '', code_postal: str = '', ville: str = '',personne:Optional[Personne] = None) -> None:
        self.__rue = rue
        self.__code_postal = code_postal
        self.__ville = ville
        self.__personne = personne
        if personne is not None:
            personne.address = self


    @property
    def _rue(self):
        return self.__rue

    @_rue.setter
    def _rue(self, value):
        self.__rue = value

    @property
    def _code_postal(self):
        return self.__code_postal

    @_code_postal.setter
    def _code_postal(self, value):
        self.__code_postal = value

    @property
    def _ville(self):
        return self.__ville

    @_ville.setter
    def _ville(self, value):
        self.__ville = value

    @property
    def _personne(self):
        return self.__personne

    @_personne.setter
    def _personne(self, value):
        self.__personne = value


# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f'{self.__rue} {self.__code_postal} {self.__ville}'
