
from typing import List
from src.models.liste_personnes import ListePersonnes
from src.models.etudiant import Etudiant
from src.models.enseignant import Enseignant
from src.models.personne import Personne


etudiant =  Etudiant(1,"john","wick",23,"master")
print("######  etudiant  ",etudiant)
etudiant.affcher_detail()


enseignant =  Enseignant(1,"mad","max",23,1500)
print("######   enseignant ",enseignant)
enseignant.affcher_detail()

ma_liste= ListePersonnes([etudiant,enseignant])
print (ma_liste[0]._nom)
ma_liste[0]._nom =  'Linux'

print (ma_liste[0]._nom)
print (etudiant)


etudiant2 =  Etudiant(2,"trotl","zomek",23,"licence")
ma_liste[0]._nom = etudiant2
print (ma_liste[0])

etudiant3 =  Etudiant(2,"trotl","zomek",23,"licence")
print(etudiant2 == etudiant3)

print('SALAIRE')
enseignant.affcher_detail()
enseignant.__iadd__(200)
enseignant.affcher_detail()