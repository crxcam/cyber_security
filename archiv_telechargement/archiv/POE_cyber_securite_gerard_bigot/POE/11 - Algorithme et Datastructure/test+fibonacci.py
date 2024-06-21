#! /usr/bin/python

import math
import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# Une autre non recursive solution
def fibo2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


# Calcule direct avec la formule de binet
def fibo3(n):
    # formule de binet : ((1 + √5)n − (1 − √5)n) / (2n√5)

    return int(
        ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2**n * math.sqrt(5))
    )


def main(n):
    print(fibo2(n))
    print(fibo3(n))


if __name__ == "__main__":
    main(42)
