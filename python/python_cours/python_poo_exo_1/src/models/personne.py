from  __future__  import annotations
from typing import Optional



class Personne:
    ___nbr_personnes:int=0
    # _     veut dire protected attribut
    # __    veut dire private attribut
    #       veut dire public

    def __init__(self, id: int = 0, nom: str = '', prenom: str = '', age: int = 0, address: Optional[Address] = None) -> None:
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__address = address
        if address is not None:
            address.personne = self
        Personne.___nbr_personnes += 1


    @staticmethod
    def nbr_personne():
        return Personne.___nbr_personnes

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

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

    @property
    def _age(self):
        return self.__age

    @_age.setter
    def _age(self, value):
        self.__age = value

    @property
    def _address(self):
        return self.__address

    @_address.setter
    def _address(self, value):
        self.__address = value




 

# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f' id:{self._id} nom:{self._nom} prenom:{self._prenom} age:{self._age} adress.rue:{self._address._rue}'

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
