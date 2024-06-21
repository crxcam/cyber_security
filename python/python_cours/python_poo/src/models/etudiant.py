from src.models.personne import Personne


class Etudiant(Personne):

    def __init__(self, id: int = 0, nom: str = '', prenom: str = '', age: int = 0, niveau: str = '') -> None:
        super().__init__(id, nom, prenom, age)
        self.__niveau = niveau

    @property
    def _niveau(self):
        return self.__niveau

    @_niveau.setter
    def _niveau(self, value):
        self.__niveau = value


    def __eq__(self, other: 'Etudiant') -> bool:
        return self._id == other._id and self._nom == other._nom

    def affcher_detail(self):
        print("Etudiant niveau ", self._niveau)


# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return super().__str__() + f' {self._niveau} '
