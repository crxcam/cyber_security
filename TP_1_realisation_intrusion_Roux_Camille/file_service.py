import os


def add_item_in_file(file_name,item,mode):
    with open(file_name,mode) as file:
            mon_fichier = open(file_name,mode) 
            mon_fichier.write(item+'\n')
            
def get_file(file_name,mode):
    return open(file_name,mode) 
    
    
def generated_file(filename,items):
    for item in items:
    	add_item_in_file(filename,item,'a')
    	
def delete_files(file_names):
    for el in file_names:
    	delete_file(el)

def delete_file(file_names):
    if os.path.exists(file_names):
        os.remove(file_names)

