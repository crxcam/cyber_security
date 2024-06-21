
from typing import Generic, TypeVar

T = TypeVar('T')


class Operation(Generic[T]):
    def __init__(self, attr1: T, attr2: T) -> None:
        self.__attr1 = attr1
        self.__attr2 = attr2

    def plus(self)-> T:
        if type(self.__attr1 and self.__attr2) == str:
            return self.__attr1+self.__attr2
        
        if type(self.__attr1 and self.__attr2) == int:
            return self.__attr1 + self.__attr2
        
        if type(self.__attr1 and self.__attr2) == bool:
            return self.__attr1 or self.__attr2
        
        return 'ERROR'

        