
import src.config.db_connexion_service as db_service



def get_all():
    connexion = db_service.get_mysql_db_connexion()
    personnes = db_service.get_all(connexion)
    for el in personnes:
        print(el)


def insert_one():
    try:
        connexion = db_service.get_db_connexion('db_connexion.json')
        db_service.insert_one('maxim', 'delanoy', connexion)
        print("insert_one succes ")
        get_all()
    except:
        print("insert_one error ")
    finally:
        if connexion.is_connected():
            connexion.close()
            print('fin de traitement')
    

