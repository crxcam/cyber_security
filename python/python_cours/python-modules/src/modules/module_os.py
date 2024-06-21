import os
import shutil


print(os.getcwd())
print(os.listdir()) # liste de repertoire 
#os.chdir('src') # changement directory
#os.mkdir("a")   # creation directory   remonte au parent
#os.makedirs('b/c/d',exist_ok=True)     # cree un arborescence 
#os.rmdir('a')    # supprimer le repertoir vide
#os.system('mkdir a')  # a faire attention si systeme support le commande
#print(os.path.exists('src/modules'))  # return true si repertoire exist
chemin = os.path.join("src","modules","module_random.py")
print(chemin)
print(os.path.exists(chemin))
print(os.path.basename(chemin)) # affiche le dernier fragment de chemin
print(os.path.isfile(chemin))
os.chdir("src")
# os.rmdir("b")
shutil.rmtree('a')  # force remove