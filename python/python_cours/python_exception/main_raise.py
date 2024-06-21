
def division(a: int, b: int) -> float:
    if type(a) is not int and  type(b) is not int:
        raise  Exception('Seul les entier sont supporté') 
    return a/b


try:
    print(division(10.2, 2.3))
except Exception as e:
    print(f"probleme division ou type  ({e})")

