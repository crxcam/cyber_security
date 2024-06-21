# pip install tinydb
from tinydb import TinyDB, Query


class GestionnaireInventaireTinyDB:
    def __init__(self, db_path):
        # Initialisation de la base de données TinyDB
        self.db = TinyDB(db_path)
        self.inventaire = self.db.table("inventaire")

    def remplir_base_de_donnees(self):
        # Insertion de documents
        self.inventaire.insert({"nom": "Pommes", "quantite": 30})
        self.inventaire.insert({"nom": "Oranges", "quantite": 20})
        print("Données insérées.")

    def interroger_base_de_donnees(self):
        # Interrogation et affichage des documents
        print("Inventaire :")
        for item in self.inventaire:
            print(item)

    def fermer_connexion(self):
        # TinyDB ne nécessite pas de fermeture explicite de connexion
        pass


if __name__ == "__main__":
    gestionnaire = GestionnaireInventaireTinyDB("db.json")
    gestionnaire.remplir_base_de_donnees()
    gestionnaire.interroger_base_de_donnees()
    gestionnaire.fermer_connexion()
