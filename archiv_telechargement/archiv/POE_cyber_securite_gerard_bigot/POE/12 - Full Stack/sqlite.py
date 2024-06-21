import sqlite3


class GestionnaireInventaire:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def creer_base_de_donnees(self):
        # Création d'une table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS inventaire
                            (id INTEGER PRIMARY KEY, nom TEXT, quantite INT)"""
        )
        self.conn.commit()

    def remplir_base_de_donnees(self):
        # Insertion de données
        self.cur.execute(
            """INSERT INTO inventaire (nom, quantite) VALUES (?, ?)""", ("Pommes", 30)
        )
        self.cur.execute(
            """INSERT INTO inventaire (nom, quantite) VALUES (?, ?)""", ("Oranges", 20)
        )
        self.conn.commit()

    def interroger_base_de_donnees(self):
        # Interrogation et affichage des données
        self.cur.execute("SELECT * FROM inventaire")
        print("Inventaire :")
        for row in self.cur.fetchall():
            print(row)

    def fermer_connexion(self):
        # Fermeture de la connexion
        self.conn.close()


if __name__ == "__main__":
    gestionnaire = GestionnaireInventaire("exemple.db")
    gestionnaire.creer_base_de_donnees()
    gestionnaire.remplir_base_de_donnees()
    gestionnaire.interroger_base_de_donnees()
    gestionnaire.fermer_connexion()
