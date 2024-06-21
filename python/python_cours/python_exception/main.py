
def division(a: int, b: int) -> float:
    return a/b

try:
    print(division(10, 2))
    print(division(10, 0))
except (ZeroDivisionError |TypeError) as e:
    print(f"probleme division ou type  ({e})")

except :
    print(f"error inconnue")
finally:
    print('FInally ')
print('Fin')
