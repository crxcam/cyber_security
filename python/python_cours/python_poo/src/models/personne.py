from abc import ABC, abstractmethod


class Personne(ABC):
    ___nbr_personnes: int = 0
    # _     veut dire protected attribut
    # __    veut dire private attribut
    #       veut dire public

    def __init__(self, id: int = 0, nom: str = '', prenom: str = '', age: int = 0) -> None:
        self._id = id
        self._nom = nom
        self._prenom = prenom
        self._age = age
        Personne.___nbr_personnes += 1

    @staticmethod
    def nbr_personne():
        return Personne.___nbr_personnes

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    id = property(get_id, set_id)

    def set_nom(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom
    nom = property(set_nom, get_nom)

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_prenom(self):
        return self.__prenom
    prenom = property(set_prenom, get_prenom)

    def set_age(self, value):
        if value < 0 or value > 150:
            self.age = 0
        else:
            self.age = value

    def get_age(self):
        return self.age

    age = property(set_age, get_age)


    @abstractmethod
    def affcher_detail():
        pass


# cela permet d'afficher object dans print


    def __str__(self) -> str:
        return f'{self._id} {self._nom} {self._prenom} {self._age}'

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
