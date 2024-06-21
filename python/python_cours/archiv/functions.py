
#from typing import Optional


import base_functions
#region-function

# est egal a la somme de divideur 
def fn_1(value:int)-> int:
    test =  True
    while value > 0:
        if not base_functions.check_if_number_is_divisible_by(value,value- 1):
            test =  False
            break
        value = value - 1
    return test  

def fn_1_correction(value:int)-> bool:
    somme = 0
    for i in range(1,value):
        if value % i ==0:
            somme+= i
    return somme == value


# function qui renvoy plusieur valeur de reponse 
def pair_impaire(liste)->tuple[int,int]:
    pairs = impaires =0
    for el in liste:
        if el %2  ==0:
            pairs +=1
        else:
            impaires += 1
            return pairs,impaires

#p,i = pair_impaire([4,3,6,5,7,8,12])
#print(f'#pair :{p} et #impaire :{i}')
#resultat = pair_impaire([4,3,6,5,7,8,12])
#print(f'#pair :{resultat[0]} et #impaire :{resultat[1]}')



def compter_voyelles_consonnes(values:str)->tuple[int,int]:
    base_functions.log_line()
    i = 0
    nb_voyelles = 0
    nb_consonne = 0
    formated =  base_functions.format_string_trim_lower(values)
    print("text a analyser :",formated)
    while i < len(formated):
        match formated[i]:
            case 'a' | 'e' | 'i' | 'o' | 'u':
                nb_voyelles += 1
            case default:
                nb_consonne += 1
        i += 1
    base_functions.log_line()
    return nb_voyelles,nb_consonne
#resultat = compter_voyelles_consonnes('aoloi usdfdsnvGSFD oue')
#print(f'#voyelles :{resultat[0]} et #consonnes :{resultat[1]}')

    
def char_in_string(char:str, values:str)->int:
    base_functions.log_line()
    print("function:char_in_string :",char,":",values)
    result = base_functions.format_string_trim_lower(values).find(char)
    if result != -1:
        base_functions.log_line()
        return result
    base_functions.log_line()
    return None

def total_characteres(*args:tuple[str])-> int:
    _concat:str = ""
    for arg in args:
            _concat += arg
    return len(_concat)


def plus_fois(a=0, b=0, c=1)->int:
    return (a + b) * c

def compute_type(*params:any)->dict:
    return base_functions.compute_type(*params) 

def operation(a:int|float, b :int|float, fn:callable)->None:
    print(fn(a,b))

def operation_1(a:int|float, b:int|float,c:int|float, fn_1:callable,fn_2:callable)->None:
    print(fn_2(fn_1(a,b),c))
#operation_1(2,3,6,lib_base.somme,lib_base.produit)
#operation(7,8,lib_base.somme)



# function lambda
somme = lambda a:int,b:int:a+b
print("result ",somme())




 
#print(compute_type('True',4,5,True,2, 5, "Bonjour", True, 'c', "3", "b", False, 10))
#print(somme(4,5,9,3))
#print(plus_fois(4,5,9))
#print("position :",char_in_string('k','mhdfhjr'))  

#print("longeur total",total_characteres('to to','bonjour'))
        
#endregion-function

