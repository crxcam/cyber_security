from typing import List
from src.models.liste_personnes import ListePersonnes
from src.models.personne import Personne
from src.models.address import Address
from src.models.personne_service import PersonneService as personne_service
from functional import seq

import src.tools.base_tools as b_tools

# personne_service = PersonneService()

# generated list of personne with random values


def init_list(nb_item: int) -> ListePersonnes:
    list_personne = []
    cpt = 0
    while cpt < nb_item:
        adresses: List[Address] = []
        nb_addresse_by_personne = b_tools.get_random_int()
        while nb_addresse_by_personne > 0:
            adresses.append(Address(b_tools.get_random_street(
            ), b_tools.get_random_zip_code(), b_tools.get_random_city()))
            nb_addresse_by_personne = nb_addresse_by_personne-1
        list_personne.append(
            Personne(b_tools.get_first_name_by_index(cpt), b_tools.get_random_sex(), adresses))
        cpt = cpt + 1
    return ListePersonnes(list_personne)


def display_list(liste_personne: ListePersonnes, msg: str):
    print(msg)
    for personne in liste_personne:
        print("="*30)
        print("nom :", personne._nom, " sexe :", personne._sex)
        print("Adresses : ")
        for adresse in personne._adresses:
            print("rue :", adresse._rue, "| code postal :",
                  adresse._code_postal, "| ville :", adresse._ville)


def search_by_nom(list_personne) -> ListePersonnes:
    x = input("Recherche personne par nom saisir la valeur de recherche : ")
    return personne_service.search_by_nom(x, list_personne)


def count_by_ville(list_personne) -> int:
    x = input("Compter par ville saisir la valeur de recherche : ")
    return personne_service.count_by_ville(x, list_personne)


def search_by_code_postal(list_personne: ListePersonnes) -> ListePersonnes:
    search_value = input(
        "Recherche personne par code postal saisir la valeur de recherche : ")
    list_personne._personnes = seq(list_personne._personnes)\
        .filter(lambda x: personne_service.code_postal_exist(search_value, x))
    return list_personne


def edit_personne(list_personne: ListePersonnes) -> ListePersonnes:
    old_nom = input(
        "Saisir ancien nom : ")
    new_nom = input(
        "Saisir nouveau nom : ")
    return personne_service.edit_personne(old_nom, new_nom, list_personne)


def app_start():
    liste_personne: ListePersonnes = init_list(4)
    print("="*30)
    display_list(liste_personne._personnes,
                 "Affichage de liste personnes au demarrage application")
    print("="*30)
    print("Recherche personne par nom choisir [1] ")
    print("Recherche personne par code postal [2] ")
    print("Compter par ville [3] ")
    print("Edit personne [4] ")
    print("Quitter [5] ")
    x = b_tools.get_and_check_if_input_is_numeric()
    fitered_list = []
    match x:
        case 1:
            fitered_list = search_by_nom(liste_personne)
            print("="*30)
            display_list(fitered_list._personnes,
                         "Affichage de liste personnes apres traitement de la demande")
        case 2:
            fitered_list = search_by_code_postal(liste_personne)
            print("="*30)
            display_list(fitered_list._personnes,
                         "Affichage de liste personnes apres traitement de la demande")
        case 3:
            print("Nombre de personne qui ont une adresse dans la ville demande : ",
                  count_by_ville(liste_personne))
        case 4:
            fitered_list = edit_personne(liste_personne)
            print("="*30)
            display_list(fitered_list._personnes,
                     "Affichage de liste personnes apres traitement de la demande")
    return


def match_fn(x, liste):
    liste_after_manage: ListePersonnes = []
    match x:
        case 1: liste_after_manage = search_by_nom(liste)
        case 2 | 3: print("result", x)

    return liste_after_manage


app_start()
# address =  Address("rue de la paix","13013","Marseille")
# print("###### object address : ",address)
# print("###### address._rue   :",address._rue)
