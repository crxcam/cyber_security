import socket
from netifaces import interfaces, ifaddresses, AF_INET
import file_service


def get_all_ifaces_with_ip():
    dicti = {}
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(
            ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        dicti.update({ifaceName: addresses})
    return dicti


def get_ip_from_virtual_network(input_ifacename):
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(
            ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        if input_ifacename == ifaceName:
            return addresses


def socket_connexion(host, port):
    result = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))  # connexion
    except OSError as e:
        result = False
    finally:
        s.close()
        return result


def discovery_network(local_ip_address, port, ip_start_index, ip_end_index, filename):
    prefix_ip = local_ip_address[0:len(local_ip_address)-3]
    cpt = ip_start_index
    cpt_ip_active = 0
    print("Start ip to scan:", prefix_ip + str(cpt),
          "end ip to scan:", prefix_ip + str(ip_end_index))
    while cpt < ip_end_index:
        ip_to_get = prefix_ip + str(cpt)
        ip_is_active = socket_connexion(ip_to_get, port)
        print("Check if ip:", ip_to_get, " is active and port",
              port, "is open :", ip_is_active)
        cpt = cpt + 1
        if ip_is_active:
            file_service.add_item_in_file(filename,  ip_to_get, 'a')
            cpt_ip_active = cpt_ip_active+1
    return cpt_ip_active
