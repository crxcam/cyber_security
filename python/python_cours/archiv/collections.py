#region-liste

def liste():
    liste = [2,3,9,7]
    print(type(list).__name__)
    print(len(liste))
    print(liste[-1])
    print(liste[-1])
    print(2 in liste)
    print(8 not in liste)
    print(8  in liste)
    liste +=[10]
    print(liste)
    liste2 = [100,liste,200]      # ajout une liste dans une listee 
    liste2 = [100,*liste,200]     # ajout 100 et 200 dans la lite equivalent ...
    liste.append(56)
    liste.insert(4,555)
   
    # suppression
    # control avant 
    if 5 in liste:
     liste.remove(5)

     # suppresion selon index 
    liste.pop(2)
    print(liste)
    #boucle 
    for el in liste:
        print(el)
        
    print("=============================")
    
    for el in reversed(liste):
        print(el)
    print("=============================")

    for el in enumerate(liste):
        print(el)
    print("=============================")

    for idx,el in enumerate(liste ,start=1):
        print(idx,el)
    print(liste.count(2))
    print(liste.index(2))
    liste.reverse()
    liste.append('Bonjour')
    liste.append('Bonjour')
    print(liste)

def exo1():
    liste =[1,2,3,2,5,1,8,7,2,2,1,2,5]
    # supprimer la deuxieme occurence de 2
    print(liste)
    print("=============================")
    found = 0
    for idx,el in enumerate(liste ,start=1):
        if el == 2:
            found += 1
            if found == 2:
                liste.pop(idx-1)
                break
    print(liste)
    
def correction_exo1():
    liste =[1,2,3,2,5,1,8,7,2,2,1,2,5]
    print(liste)
    print("=============================")
    first_index = liste.index(2)
    second_index = liste.index(2,first_index+1)
    liste.pop(second_index)
    print(liste)

def exo2():
    liste =[1,2,3,2,5,1,8,7,2,2,1,2,5]
    liste.reverse()
    print(liste)
    print("=============================")
    first_index = liste.index(2)
    second_index = liste.index(2,first_index+1)
    liste.pop(second_index)
    print(liste)

def liste2():
    liste =[]
    liste2 = list()
    liste3 = [0 for _ in range(10)]
    liste4 = [x for x in range(11)]
   
 
    print(liste)
    print(liste4)

    

#endregion-liste

#region-tuple liste de constant

def tuple():
    mon_tuple= (1,2,3,5)
    for el in mon_tuple:
        print(el)

    

#endregion-tuple

#region-ensemble

def ensemble_fn():
    ensemble = {4,5,6,8,2}
    print(len(ensemble))
    print(ensemble)
   
    ensemble.add(89)
    ensemble.add(1)
    ensemble.remove(1)
    ensemble.discard(8)
    print(ensemble)

def ensemble_fn2():
    set1 = {4,5,6,8,2}
    set2 = {7,5,66,8,2}
    print('set1 : ',set1)
    print('set2 : ',set2)
    print("intersection(set2) :",set1.intersection(set2))
    print("set1 & set2 :",set1 & set2)
    print("set1 | set2:", set1 | set2)
    print("set1.union(set2) :", set1.union(set2))
    print("set1.difference(set2) :", set1.difference(set2))
    print("set1.issubset(set2) :", set1.issubset(set2))
    print("set1.issuperset(set2) :", set1.issuperset(set2))
    print("set1.isdisjoint(set2) :", set1.isdisjoint(set2))


def ensemble_exo():
    #verifie que l’intersection entre ´ ensemble3 et ensemble2 est un sous-ensemble d ensemble1
    ensemble1 = {2, 3, 8, 5}
    ensemble2 = {7, 2, 9, 3}
    ensemble3 = {1, 2, 4, 5}
    print("verifie que l’intersection entre ´ ensemble3 et ensemble2 est un sous-ensemble d ensemble1")
    print("### => :",ensemble1.issubset(ensemble2.intersection(ensemble3)))
    # correction 
    print("### => :",ensemble3.intersection(ensemble2.issubset(ensemble1)))
    print("### => :",((ensemble3 & ensemble2) <= ensemble1))
    print("=============================")
    print("affiche les valeurs presentes dans ´ ensemble1 ou ensemble2 mais pas dans ensemble3 ")
    print("### => :",ensemble3.difference(ensemble1 | ensemble2))
    # correction 
    print("### => :",ensemble1.union(ensemble2).difference(ensemble3))
    print("### => :",((ensemble1 | ensemble2) - ensemble3))
    print("=============================")
    print(" affiche les valeurs presentes dans ´ ensemble1 et ensemble2 mais pas dans ensemble3 ")
    print("### => :",ensemble3.difference(ensemble1 & ensemble2))
     # correction 
    print("### => :",ensemble1.intersection(ensemble2).difference(ensemble3))
    print("### => :",((ensemble1 & ensemble2) - ensemble3))
    
    print("=============================")
    print(" affiche les valeurs presentes dans ´ ensemble1 ou ensemble2 mais pas dans les deux ensembles a la fois  ")
     # correction 
    set4 = {} # cree un dictionnaire 
    set4 = set() # cree un ensemble

   

 


#endregion-ensemble

#region-dictionnaie
def dico_01():
    languages={
    "python":10,
    "java":8,
    "c++":5,
    "c#":2,
        }
    print(languages)
    print("languages.get('java')) => :",languages.get('java'))
    print("languages['java'] => :",languages['java'])
    print("languages.keys() => :",languages.keys())
    print("languages.values() => :",languages.values())
    print('java' in languages)
    print('java' in languages.keys())
    print("len(languages) => :",len(languages))
    languages['php'] = 4
    print(languages)
    languages.update({'c':2,'java':9})
    languages.pop('php')
    print("languages.pop('php') => " ,languages)

    for key,value in languages.items():
        print("key",key," value",value)
        
    for key in languages:
        print("key",key," value",languages[key])




def dicto_exo_01():
#Ecrire un programme ´ Python qui permet de rep´ eter l’affichage de chaque cl ´ e de ce dictionnaire ´selon la valeur associee
    repetition = {
    "Java": 2,
    "PHP": 5,
    "C++": 1,
    "HTML": 4
    }

    keys = repetition.keys()
    for key in repetition:
        cpt = 0
        nb = int(repetition[key])
        print("nombre ",nb)
        while cpt <= nb:
            print("key",key," value",repetition[key])
            cpt += cpt + 1
    #correction
    print("correction")
    for key,value in repetition.items():
        print(key * value, end =" ")
    

def dicto_exo_01():
    liste = [2, 5, "Bonjour", True, 'c', "3", "b", False, 10]
    dico={}
    
    for el in liste:
        if not type(el).__name__ in dico:
             dico.update({type(el).__name__ :1})
        else:
             val = dico[type(el).__name__ ]
             val += 1
             dico.update({type(el).__name__ :val})       
        
    print("Result => ",dico)

    
#endregion-dictionnaie

#def muabla():
   # chaine = 'bonjour'
    #chaine.replace('b','B')
    #print("Result => ",id(chaine))
     
#muabla()
