from enum import Enum

class Animal(Enum):
    CHAT=1
    CHIEN=7
    CHEVAL=5
    LOUP=3


if __name__ == '__main__' :
    print(Animal.CHEVAL.value)