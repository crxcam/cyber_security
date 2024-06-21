
from enum import Enum
from typing import List
from functional import seq

from src.models.liste_personnes import ListePersonnes
from src.models.personne import Personne
import src.tools.base_tools as b_tools


class Sex(Enum):
    M = 'M'
    F = 'F'


class PersonneService:

    def search_by_nom(search_value: str, list_personne: ListePersonnes) -> ListePersonnes:
        list_personne._personnes = seq(list_personne._personnes)\
            .filter(lambda x: search_value.lower() in x._nom.lower())
        return list_personne

    def code_postal_exist(search_value: str, personne: Personne) -> bool:
        test = False
        for el in personne._adresses:
            if el._code_postal == search_value:
                test = True
                break
        return test


    def count_by_ville(search_value: str, list_personne: ListePersonnes) -> int:
        cpt = 0
        found = False
        for personne in list_personne._personnes:
            if b_tools.ville_exist(search_value, personne):
                cpt += 1
        return cpt

    def search_by_sex(search_value: Sex, personnes: List[Personne]) -> List[Personne]:
        return filter(lambda x: x._sex == search_value, personnes)
    
    def edit_personne(old_nom:str,new_nom:str,list_personne: ListePersonnes)->  ListePersonnes:
        for personne in list_personne._personnes:
            if personne._nom == old_nom:
                personne._nom = new_nom
        return list_personne

