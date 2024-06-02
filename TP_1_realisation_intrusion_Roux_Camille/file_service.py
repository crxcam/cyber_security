
def add_item_in_file(file_name,item,mode):
    with open(file_name,mode) as file:
            mon_fichier = open(file_name,mode) 
            mon_fichier.write(item+'\n')
            
def get_file(file_name,mode):
    return open(file_name,mode) 
    
    
def generated_file(filename,items):
    for item in items:
    	add_item_in_file(filename,item,'a')
