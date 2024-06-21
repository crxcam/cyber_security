



def fichier(file_name:str,mode:str):
    with open(file_name,mode) as file:
            #mon_fichier = open('./mon_fichier.txt','w') # ecrase
            #mon_fichier = open('./mon_fichier.txt','a') # ajout contenue
            #mon_fichier = open('./mon_fichier.txt','r') # lire  contenue
            #mon_fichier.write('hello')
       print("buffer file.buffer.name : ",file.buffer.name) 
       print("file.read() : ",file.read()) 


fichier("./mon_fichier.txt","r")

def gererated_script_file(port):
    file_ip = open("./ip_address.txt", 'r')
    addresses = file_ip.readlines()

    file_login_pswd = open("./login_pswd.txt", 'r')
    logins_pswds = file_ip.readlines()

    cmd= "use auxiliary/scanner/ssh/ssh_login "
    for address in addresses:
        cmd += "set RHOST " +address + "set RPORT "+port
        for line in logins_pswds:
            splited= line.split(":")
            cmd += " set USERNAME " + splited[0]
            cmd += " set PASSWORD " + splited[1]
            cmd += " run"
            result = subprocess.run("ls", shell=True, capture_output=True, text=True)
    print('FIN')

def save_cmds_in_file(cmds):
    for cmd in cmds:
      add_in_file("./script.txt", cmd,'a')