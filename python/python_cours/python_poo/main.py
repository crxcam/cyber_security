
from typing import List
from src.models.etudiant import Etudiant
from src.models.enseignant import Enseignant
from src.models.personne import Personne


#print("######    ",personne1)
personne1 = Personne(2,'max','cornel',45)
#print("######    ",personne2)
#print("######    ",personne2.get_nom())
#print("######    ",personne2.get_nom())

etudiant =  Etudiant(1,"john","wick",23,"master")
print("######  etudiant  ",etudiant)


enseignant =  Enseignant(1,"mad","max",23,1500)
print("######   enseignant ",enseignant)

personnes :List[Personne] = [personne1,etudiant,enseignant]

for item in personnes:
    if isinstance(item,Personne):
        print('Instance de Personne')
    if isinstance(item,Enseignant):
        print('Instance de Enseignant',item._salaire)
    if isinstance(item,Etudiant):
        print('Instance de Etudiant',item._niveau)


