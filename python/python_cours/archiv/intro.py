import base_functions

def check_type():
    a = 1
    b = 5
    a, b = b, a
    # definir type
    print(type(a).__name__)
    print(isinstance(a, int))


def permutation():
    a = 1
    b = 5
    print(a)
    print(b)
    a, b = b, a
    print(a)
    print(b)


def chaine():
    chaine = 'Test bonjour!'
    print(chaine * 2)
    print(chaine[0:2])
    print(chaine[2:])
    print(len(chaine))
    print(chaine.replace('jour', 'soir'))
    print(chaine.split())
    chaine = 'bonjour tout le monde'
    print(chaine.capitalize())
    print(chaine.title())
    print(chaine.find('n'))
    print('chaine.find', chaine.find('o', 2))
    print('chaine.startswith', chaine.startswith('bo'))
    print('chaine.count', chaine.count('o'))
    print('chaine.isalpha', chaine.isalpha())
    print('chaine.isascii', chaine.isascii())
    print('chaine.isnumeric', chaine.isnumeric())
    print('chaine.isspace', chaine.isspace())
    del chaine
    print(chaine)


def build_numeric_array_from_input(nb_input):
    arr = []
    while nb_input > 0:
        arr.append(get_and_check_if_input_is_numeric())
        nb_input = nb_input-1
    return arr


def check_input_somme_is_paire(nb_input):
    arr = build_numeric_array_from_input(nb_input)
    somme = 0
    for i in arr:
        somme = somme + i
    print('paire' if base_functions.check_if_number_is_divisible_by(
        int(somme), 2) else 'impaire')


def match_fn():
    x = 10
    match x:
        case 1: print("result", x)
        case 2 | 3: print("result", x)
        case 5: print("result", x)
        case defaut: print("autre")
    print("fin")


def calc_day():
    x = int(input("Saisir numero de mois : "))
    match x:
        case 4 | 6 | 9 | 11:
            print("nombre jours 30")
        case 2:
            y = int(input("Saisir anne: "))
            print("lib_base.check_if_number_is_divisible_by(y, 4)",
                  base_functions.check_if_number_is_divisible_by(y, 4))
            print("lib_base.check_if_number_is_divisible_by(y, 400)",
                  base_functions.check_if_number_is_divisible_by(y, 400))
            print("lib_base.check_if_number_is_divisible_by(y, 100)",
                  base_functions.check_if_number_is_divisible_by(y, 100))
            if base_functions.check_if_number_is_divisible_by(y, 4) and base_functions.check_if_number_is_divisible_by(y, 400) and not base_functions.check_if_number_is_divisible_by(y, 100):
                print("nombre jours 29")
            else:
                print("nombre jours 28")
        case defautl: print("nombre jours 31")
    print("fin")


def match_detail():
    x = 0
    a, b = 2, -1
    match a:
        case a if a > 0:
            print("positif")
        case a if a < 0:
            print("negatif")
    match a, b:
        case a, b if a > 0 and b > 0:
            print("positif")
        case a, b if a < 0 and b < 0:
            print("negatif")
        case default:
            print("autres")
    print("fin")


def boucle_while():
    cpt = 0
    while cpt < 10:
        if base_functions.check_if_number_is_divisible_by(cpt, 2):
            print(cpt, 'est divisible par 2 ')
        cpt += 1


def boucle_while_exo():
    x = input("Saisir un text : ")
    i = 0
    nb_voyelles = 0
    while i < len(x):
        match x[i]:
            case 'a' | 'e' | 'i' | 'o' | 'u':
                print("result", x)
                nb_voyelles += 1
        i += 1

    print("nombre voyelle ", nb_voyelles)

def boucle_while_exo2():
    x = input("Saisir un text : ")
    if "a" or "e" or "i" or "o"  or "u"   in x: 
       print("text contient voyelle ")


def boucle_for_exo1(nb_value):
    arr = build_numeric_array_from_input(nb_value)
    i = arr[0]
    while i > 0:
        if base_functions.check_if_number_is_divisible_by(arr[0],i) and base_functions.check_if_number_is_divisible_by(arr[1],i):
            print("diviseur commun ",i)
            break
        i = i-1  
    else:
         print("pas de divideur commun ")
     
        


 
boucle_for_exo1(2)
