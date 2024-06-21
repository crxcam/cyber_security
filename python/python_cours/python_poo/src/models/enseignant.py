from src.models.personne import Personne

class Enseignant(Personne):

    def __init__(self, id: int = 0, nom: str = '', prenom: str = '', age: int = 0, salaire: float =0) -> None:
        super().__init__(id, nom, prenom, age)
        self.__salaire = salaire

    @property
    def _salaire(self):
        return self.__salaire

    @_salaire.setter
    def _salaire(self, value):
        self.__salaire = value

    def affcher_detail(self):
        print("enseignant salaire ",self.__salaire)

    def __iadd__(self, i: int) -> bool:
        self.__salaire += i
        return self

    


# cela permet d'afficher object dans print

    def __str__(self) -> str:
          return super().__str__() + f' {self._salaire} '

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
