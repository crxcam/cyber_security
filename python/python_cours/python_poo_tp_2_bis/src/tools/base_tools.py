import random

from src.models.personne import Personne


fisrt_names = ["John", "Max", "Alex", "Igor", "Guillame", "Camille",
               "Vincent", "Joseph", "Philippe", "Eva", "Michelle", "Marion"]
last_names = ["Wick", "Mad", "Doe", "Yashin", "Lotbrok", "Rollo",
              "Maximus", "Nycz", "Stalin", "Dupont", "Washik", "Sabaton"]
ages = [45, 78, 15, 25, 14, 78, 96, 26, 36, 58, 47, 45, 6, 54, 8]
random_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

strets = ["14 rue de la paix", "15 rue de la paris",
          "8 rue de la guerre", "14 rue de la bordeaux"]
zipcodes = ["13013", "75026", "78563", "45213"]
cities = ["Paris", "Marseille", "Bordeaux", "Lille",
          "Le Mans", "Gemenos", "Aix en provence"]

sex = ['F', 'M']


def get_and_check_if_input_is_numeric() -> int:
    is_valid = True
    while is_valid:
        x = input("Saisir un nombre : ")
        if x.isnumeric():
            is_valid = False
        else:
            print(x, ": n'est pas un nombre recommencer !!")
    return int(x)


def get_random_first_name() -> str:
    return random.choice(fisrt_names)


def get_first_name_by_index(index: int) -> str:
    return fisrt_names[index]


def get_random_last_name() -> str:
    return random.choice(last_names)


def get_random_sex() -> str:
    return random.choice(sex)


def get_random_age() -> int:
    return random.choice(ages)


def get_random_street() -> str:
    return random.choice(strets)


def get_random_city() -> str:
    return random.choice(cities)


def get_random_zip_code() -> str:
    return random.choice(zipcodes)


def get_random_int() -> int:
    return random.choice(random_int)

def ville_exist(search_value: str, personne: Personne) -> bool:
        test = False
        for el in personne._adresses:
            if el._ville.lower() == search_value.lower():
                test = True
                break
        return test
