from functional import seq

numbers = [1, 9, 8, 6, 4]


def carree(x: int) -> int:
    return x*x


def est_paire(x: int) -> int:
    return x % 2 == 0


print(list(map(carree, numbers)))

marques = ["peugeot", "fiat", "mercedes"]
print(list(map(lambda x: len(x), marques)))


print(list(filter(est_paire, numbers)))

print(list(filter(lambda x: x % 2 == 0, numbers)))

print(list(filter(lambda x: len(x) % 2 == 0, marques)))

resultat = seq(marques)\
    .map(len)\
    .filter(lambda x: x % 2 == 0)\
    .for_each(print)
