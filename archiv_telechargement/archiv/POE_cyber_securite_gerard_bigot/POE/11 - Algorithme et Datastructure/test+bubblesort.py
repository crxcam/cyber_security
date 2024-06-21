import random


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Créer un tableau de 20 entiers aléatoires entre 0 et 99999
random_numbers = [random.randint(0, 99999) for _ in range(20)]

# Afficher le tableau non trié
print("Tableau non trié:")
print(random_numbers)

# Trier le tableau avec le tri à bulle
bubble_sort(random_numbers)

# Afficher le tableau trié
print("\nTableau trié:")
print(random_numbers)
