def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  # Trouver le point milieu
        left_half = array[:mid]  # Diviser les éléments en 2 moitiés
        right_half = array[mid:]

        merge_sort(left_half)  # Tri récursif de la première moitié
        merge_sort(right_half)  # Tri récursif de la seconde moitié

        i = j = k = 0

        # Copier les données dans les tableaux temporaires left_half et right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Vérifier si des éléments ont été laissés
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

# Exemple d'utilisation
array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(array)
print("Tableau trié :", sorted_array)
