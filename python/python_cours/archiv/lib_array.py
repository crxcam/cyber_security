
#   function calc moyen in array integer #

def calc_moyen(items):
    a = 0
    for item in items:
        a = a + item
    return (a / items.len)

#   function create array with number #


def create_array_with_number(nb_of_element):
    cpt = 0
    arr = []
    while cpt < nb_of_element:
        arr.append(cpt)
        cpt = cpt + 1

    return arr

#   function create array number two dimension #


def create_array_number_two_dimension(x, y):
    cpt = 0
    #    define array
    rows, cols = (len(x), 2)
    # init array
    arr = [[0]*cols]*rows
    while cpt < len(x):
        arr[cpt] = [x[cpt], y[cpt]]
        cpt = cpt+1
    return arr


def calc_produit_in_array_two_dimension(x, y):
    cpt = 0
    arr = create_array_number_two_dimension(x, y)
    arr_result = []
    while cpt < len(x):
        arr_result.append()
        cpt = cpt+1
    return arr


def search_max_value_in_integer_array(array):
    return max(array)

#   output only positive element in integer array #


def get_positive_element_in_integer_array(array):
    result = filter(lambda x: x > 0, array)
    return list(result)


def find_value_in_array(array, value):
    match = False
    for i in array:
        if i == value:
            match = True
            break

    return match


def sort_integer_array(array, is_descending):
    array.sort(reverse=is_descending)
    return array

def get_nb_occurence_in_array(items, search_value):
    result = filter(lambda x: x == search_value, items)
    return len(list(result))

def boucle_for_in():
    c = ["Marc", "est", "dans", "le", "jardin"]
    for i in c:
        print("i vaut", i)


def boucle_while():
    x = 1
    while x < 10:
        print("x a pour valeur", x)
        x = x * 2
        print("Fin")


def boucle_for_with_break():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break
