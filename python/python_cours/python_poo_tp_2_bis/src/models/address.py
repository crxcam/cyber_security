from  __future__  import annotations

from typing import Optional




class Address:

    def __init__(self, rue: str = '', code_postal: str = '', ville: str = '') -> None:
        self.__rue = rue
        self.__code_postal = code_postal
        self.__ville = ville


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

# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f'{self.__rue} {self.__code_postal} {self.__ville}'
