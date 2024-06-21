class Person:

    # _     veut dire protected attribut
    # __    veut dire private attribut
    #       veut dire public

    def __init__(self, id: int = 0, nom: str = '', prenom: str = '', age: int = 0) -> None:
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.age = age

    @property
    def id(self):
        return self.__id
    
    @id.setter 
    def id(self, id):
        self.__id = id

    @property
    def nom(self):
        return self.__nom

    @nom.setter 
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter 
    def prenom(self, prenom):
        self.__prenom = prenom
    @property
    def age(self):
        return self.__age

    @age.setter  
    def age(self, value):
        if value < 0 or value > 150:
            self.__age = 0
        else:
            self.__age = value


    


# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f'{self.id} {self.nom} {self.prenom} {self.age}'

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
