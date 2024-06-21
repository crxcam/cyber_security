from src.models.personne import Personne
from src.models.address import Address


# creation object adreee 
# tester acces 
# ajout attribut addresse a la classe Personne 
# creation de prsonne avec adresse 
# test acess

address =  Address("rue de la paix","13013","Marseille")
print("###### object address : ",address)
print("###### address._rue   :",address._rue)
personne = Personne(1,"mad","max",21,address)
print("###### object personne : ",personne)
print("###### personne._address._rue    ",personne._address._code_postal)
personne._address._code_postal = "75001"
print("###### personne addresse modifier    ",personne._address._code_postal)
print("###### address.personne    ",address.personne)