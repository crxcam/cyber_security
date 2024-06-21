import copy

liste = [1,2,3,4]
liste2 = copy.deepcopy(liste)
liste[0]=10
print(liste2[0])