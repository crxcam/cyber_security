
from typing import Iterable, Optional
from src.config.my_connexion import MyConnexion
from src.dao.generic_dao import GenericDao
from src.models.personne import Personne


class PersonneDao (GenericDao[Personne]):
    __db = None

    def __init__(self) -> None:
        self.__db = MyConnexion()

    def save(self, personne: Personne) -> Personne:
        query = 'insert into personne (nom,prenom) values(%s,%s)'
        params = [personne._nom, personne._prenom]
        return self.__db.query(query,params).s()


    def update(self, personne: Personne) -> Personne:
        pass

    def delete(self, personne: Personne) -> None:
        pass

    def find_all(self) -> Iterable[Personne]:
        return self.__db.query('select * from personne').fetchall()

    def find_by_id(self, id) -> Optional[Personne]:
        query = 'select * from personne where num = %s'
        params=[id]
        return self.__db.query(query,params).fetchone()
