
# region :check function

# get value from console and check if is int
def get_and_check_if_input_is_numeric()-> int:
    is_valid = True
    while is_valid:
        x = input("Saisir un nombre : ")
        if x.isnumeric():
            is_valid = False
        else:
            print(x, ": n'est pas un nombre recommencer !!")
    return int(x)


def input_is_list(value)-> bool:
    if type(value) == list:
        return True
    else:
        return False

def factorielle(n:int|float)-> int|float:
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n-1)
    
def fibonacci(n:int|float) -> int|float:
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


#   function check if number is possible / by divider #
def check_if_number_is_divisible_by(number:int, divider:int)-> bool:
    res:int = number % divider
    if res == 0:
        return True
    else:
        return False

# endregion :check function

# region :log
def log_line()->None:
  print("==========================================")

# endregion :log

def format_string_trim_lower(values:str) -> str:
    return values.lower().replace(" ", "")

#   compute type of args #
def compute_type(*params:any)->dict:
    dico:dict={}
    
    for el in params:
        if not type(el).__name__ in dico:
             dico.update({type(el).__name__ :1})
        else:
             val = dico[type(el).__name__ ]
             val += 1
             dico.update({type(el).__name__ :val})       
        
    log_line()
    return dico

def somme(*args:tuple[int|float])->int|float:
    resultat:int=0
    for arg in args:
        resultat += arg
    return resultat

def produit(a:int|float, b:int|float)->int|float:
    return a * b


def calc_factorielle(input:int|float)-> int|float:
    result:int|float = input
    if input == 1 | input == 0 | input < 0:
        return result
    else:
        while input > 0:
            input = input - 1
            if input > 0:
                result = input * result
        return result

def calc_if_first_number_divider(input:int|float)-> bool:
    is_first:bool = True
    if input == 1 | input == 0 | input < 0:
        return is_first
    else:
        for i in range(2, i-1):
            if (i-1) % i == 0:
                is_first = False
        return is_first
