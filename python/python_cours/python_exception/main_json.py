

import json 
import os
content ={}
def fichier_json(file_name:str):
    print(os.listdir())
    with open('python_exception/file.json') as file:
            
            content = json.load(file)
            #mon_fichier = open('./mon_fichier.txt','w') # ecrase
            #mon_fichier = open('./mon_fichier.txt','a') # ajout contenue
            #mon_fichier = open('./mon_fichier.txt','r') # lire  contenue
            #mon_fichier.write('hello')
            print("content : ",content["nom"]) 
             


fichier_json("fichier.json")