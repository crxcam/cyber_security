
from src.exceptions.code_postal_exception import CodePostalException
from src.models.address import Address

try:
    addresse = Address('rue', '12022', "lyon")
except CodePostalException as e:
    print(f"catch exception : ", e)
finally:
    print('Finally ')
print('Fin')

import socket

def get_my_ip_from_virtual_network():
 for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        print (ifaceName, ', '.join(addresses))

def app_start():
    print("start application")
    all_iface_and_ip= tp_tools.get_all_ifaces_with_ip()
    print("result :",all_iface_and_ip)
    tp_tools.discovery_network(all_iface_and_ip['eth1'][0],22,125,130)

def generated_login_pswd_file(file_name,  input_string:str):
    logins_pswd:['user:password','toto:test123','admin:admin','admin:password']