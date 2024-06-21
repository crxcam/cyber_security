import importlib ,locale

print(locale.getlocale()[0])
langue = 'fr' if locale.getlocale()[0] == 'fr_FR' else 'en_EN'
module =  importlib.import_module(langue) ## export module ici le module(fichier) se nomme soit(fr.py ou en.py)


module.salutation()   # recupere la methode qui doit existe dans module